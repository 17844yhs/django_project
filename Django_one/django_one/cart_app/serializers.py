import datetime
from rest_framework import serializers
from .models import Category,Goods,Cart,CartItem
from user_app.models import User
from django.db import transaction
# 为了一查多
class UtilsCategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class GetGoodSerialize(serializers.ModelSerializer):
    category = UtilsCategorySerialize()
    class Meta:
        model = Goods
        fields = '__all__'

class GetCategorySerialize(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    subcategories = UtilsCategorySerialize(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','subcategories','count']
    def get_count(self, obj):
        return obj.goods.count()  # 假设 Category 模型有一个 related_name='goods' 的关联字段


class CartItemSerializer(serializers.ModelSerializer):
    # 商品详情（使用你已有的 GetGoodSerialize）
    goods = GetGoodSerialize(read_only=True)
    # 小计金额（自动计算单价×数量）
    subtotal = serializers.DecimalField(
    read_only=True,
    max_digits=19,
    decimal_places=2
)
    # 最大可购买数量（基于库存）
    max_quantity = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CartItem
        fields = [ 
            'id',
            'goods', 
            'quantity', 
            'subtotal',
            'max_quantity',
            'added_at'
        ]
        read_only_fields = ['added_at']
    def get_max_quantity(self, obj):
        """返回当前商品的最大可购买数量（库存）"""
        return obj.goods.stock
    
class GetMyCartSerialize(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)  # 使用专门的CartItem序列化器
    total_price = serializers.DecimalField(max_digits=19, decimal_places=2, read_only=True)
    total_items = serializers.IntegerField(read_only=True)

    class Meta:
        model = Cart  # 使用Cart模型而非CartItem
        fields = ['created_at', 'updated_at', 'items', 'total_price', 'total_items']
        read_only_fields = ['created_at', 'updated_at']

class CartItemUpdateSerializer(serializers.ModelSerializer):
    goods_id = serializers.PrimaryKeyRelatedField(
        queryset=Goods.objects.all(), 
        source='goods',
        write_only=True
    )
    quantity = serializers.IntegerField(min_value=1, max_value=100)
    
    # 新增：接收用户标识（手机号或用户ID）
    phone = serializers.CharField(write_only=True, required=False)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = CartItem
        fields = ['goods_id','phone', 'user_id', 'quantity',]  # 添加用户标识字段

    def validate(self, attrs):
        """业务逻辑验证"""
        # 获取商品和数量
        # 视图层可以访问的原始数据
            # request.data == {
            #     'goods_id': 123,  # 前端发送的是ID
            #     'quantity': 2
            # }
        # 经过 PrimaryKeyRelatedField 转换后
            # attrs == {
            #     'goods': <Goods object id=123>,  # 已变成模型对象
            #     'quantity': 2
            # }
        # 获取新的goods，attrs['goods'] 是本次请求想要更新/设置的新商品对象
        goods = attrs['goods']
        quantity = attrs['quantity']
        
        # --- 用户验证逻辑 ---
        phone = attrs.pop('phone', None)
        user_id = attrs.pop('user_id', None)
        
        if not (phone or user_id):
            raise serializers.ValidationError({
                'status': '404',
                'detail': '必须提供用户标识（手机号或用户ID）'
            })
        
        try:
            if phone:
                user = User.objects.get(phone=phone)
            else:
                user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'status': '404',
                'msg': '用户不存在'
            })
        
        # --- 购物车验证 ---
        cart,created = Cart.objects.get_or_create(user=user)  # 获取或创建购物车
        attrs['carts'] = cart  # 将cart存入验证后的数据
        
        # --- 库存验证 ---
        if quantity > goods.stock:
            raise serializers.ValidationError({
                'status': '500',
                'msg': '库存不足',
                'available': goods.stock,
                'requested': quantity
            })

        # --- 重复商品验证 ---
          # 2. 智能重复检查  
        if self.instance:  # 更新操作 只有当商品ID发生变化时才检查重复（因为用户可能只是修改数量）
            # 关键判断：只有goods_id变化时才检查重复，self.instance 是当前正在被更新的 CartItem 对象（购物车商品项）
            if 'goods' in attrs and attrs['goods'].id != self.instance.goods.id:
                #1.检查是否传入了新的商品：
                # 如果用户没有修改商品（只传了 quantity），attrs 可能没有 'goods' 键
                # 只有用户修改了商品时，attrs 才会包含 'goods'
                #2.新旧商品对比：
                # 如果传入了新商品（'goods' in attrs为True）
                # 且新商品ID与旧商品ID不同（attrs['goods'].id != self.instance.goods.id）
                # 才需要检查是否重复
                if CartItem.objects.filter(carts=cart, goods=goods).exists():
                    raise serializers.ValidationError({
                        'status': 400,
                        'code': 'spec_already_exists',
                        'msg': '该规格商品已在购物车'
                    })
        else:  # 新增操作 直接检查购物车中是否已存在相同的商品
            if CartItem.objects.filter(carts=cart, goods=goods).exists():
                raise serializers.ValidationError({
                    'status': 400,
                    'code': 'goods_already_in_cart',
                    'msg': '商品已在购物车' 
                })

        return attrs
    @transaction.atomic
    def create(self, validated_data):
        """创建商品项"""
        # 规范一下cart名字仅仅
        cart = validated_data.pop('carts')
        return CartItem.objects.create(carts=cart, **validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        # 如果传入了新商品，且新旧商品不同 → 替换模式
        if 'goods' in validated_data and instance.goods.id != validated_data['goods'].id:
            instance.delete()  # 删除旧商品 这就是t_cartitem.id会变化的原因
            return CartItem.objects.create(**validated_data)  # 创建新商品项
        # 否则正常更新数量
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance
    
    def to_representation(self, instance):
        """统一响应格式"""
        data = super().to_representation(instance)
        return {
            "code": 200,
            "data": data,  # 原始数据
            "meta": {
                "operation": "update",
                "timestamp": datetime.datetime.now()
            }
        }