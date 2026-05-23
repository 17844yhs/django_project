from django.db import models
from user_app.models import User
from rest_framework import serializers
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32,verbose_name='分类名称')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='subcategories',
        verbose_name='父级分类')
    class Meta:
        db_table = 't_category'
        verbose_name = '商品分类'
        verbose_name_plural = '商品分类'
        unique_together = ('name', 'parent')  # 确保同一层级分类名称唯一

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name    
    
class Goods(models.Model):
    TYPE_CHOICES = [
        (0, 'new'),
        (1, 'hot'),
    ]
    badgeType = models.CharField(choices=TYPE_CHOICES,max_length=12,null=True,blank=True,default='hot',verbose_name='商品销售程度')
    name = models.CharField(max_length=32,verbose_name='商品名称')
    price = models.DecimalField(max_digits=19,decimal_places=2,verbose_name='商品价格')
    description = models.TextField(verbose_name='商品描述', blank=True,null=True)
    stock = models.IntegerField(default=0, verbose_name='商品库存')
    pic = models.CharField(max_length=255, null=True,blank=True,verbose_name='商品图片')
    address = models.CharField(max_length=64, null=True,blank=True,verbose_name='商品地址')

    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='goods',
        verbose_name='商品分类'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        db_table = 't_goods'
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.OneToOneField(User,models.CASCADE,verbose_name='用户',related_name='cart',primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    class Meta:
        db_table = 't_carts'

    def __str__(self):
        return f"{self.user.nick_name}的购物车"
    @property
    def total_price(self):
        """计算购物车中所有商品的总价"""
        return sum(item.subtotal for item in self.items.all())

    @property
    def total_items(self):
        """计算购物车中商品总数量"""
        return sum(item.quantity for item in self.items.all())
class CartItem(models.Model):
    carts = models.ForeignKey(Cart,models.CASCADE,related_name='items',verbose_name='购物车')
    goods = models.ForeignKey(Goods,models.CASCADE,verbose_name='商品')
    # PositiveIntegerField 经常用于需要存储非负整数的场景，比如数量、价格、计数器等
    quantity = models.PositiveIntegerField(default=1, verbose_name='数量')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    class Meta:
        db_table = 't_cartitem'
        verbose_name = '购物车商品'
        verbose_name_plural = '购物车商品'
        unique_together = ('carts', 'goods')  # 同一商品在购物车中只能有一条记录
    
    def __str__(self):
            return f"{self.quantity}x{self.goods.name}"

    @property
    def subtotal(self):
        """计算当前商品项的小计（单价×数量）"""
        return self.goods.price * self.quantity
    
    def save(self, *args, **kwargs):
        if self.quantity > self.goods.stock:
            raise serializers.ValidationError("商品库存不足")
        super().save(*args, **kwargs)