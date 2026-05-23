from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status

from .serializers import GetCategorySerialize,GetGoodSerialize,GetMyCartSerialize,CartItemUpdateSerializer
from .models import Category,Goods,Cart,CartItem
from user_app.models import User
from utils.pyjwt import encode_jwt,decode_jwt
# Create your views here.

class GetCategory(APIView):
    def get(self,request):
        # 查询所有一级分类数据
        categorys = Category.objects.all().order_by('id')
        #  创建序列化器
        ser = GetCategorySerialize(categorys,many=True)
        return Response(ser.data)


def get_all_subcategories(category):
    """递归获取某个分类的所有子分类（包括子分类的子分类，无限层级）"""
    subcategories = list(category.subcategories.all())  # 获取直接子分类
    for sub in category.subcategories.all():  # 递归获取子分类的子分类
            subcategories.extend(get_all_subcategories(sub))
    return subcategories

class GetGoodsByName(APIView):
    def get(self,request):
        try:
            name = request.query_params.get('name')
            if name:
                goods = Goods.objects.filter(name__contains=name)
            else:
                goods= Goods.objects.all()
            # 创建序列化器
            ser = GetGoodSerialize(goods, many=True)
            return Response({'status':200,'data':ser.data,'msg':'返回商品数据成功'})
        except Exception as e:
            return Response({"status":500,'msg':'获取商品详情失败'})

class GetGoodsBycategory(APIView):
    def get(self, request):
        try:
            category_id = request.query_params.get('id')
            if category_id:
                category_id = int(category_id)
                category = Category.objects.get(id=category_id)
                
                # 获取该分类及其所有子分类（无限层级）
                all_categories = [category] + get_all_subcategories(category)
                
                # 查询这些分类下的商品
                goods = Goods.objects.filter(category__in=all_categories)
            else:
                goods = Goods.objects.all()
            ser = GetGoodSerialize(goods, many=True)
            return Response({
                'status': 200,
                'data': ser.data
            })
        except Category.DoesNotExist:
            return Response({
                'status': 404,
                'msg': '分类不存在'
            })
        except Exception as e:
            return Response({
                'status': 500,
                'msg': '获取失败'
            })
        
# class GetCart(APIView):
#     def get(self,request):
#         # 获取传递来的手机号
#         phone =request.query_params.get('phone')
#         try:
#             # 获取用户
#             user = User.objects.get(phone =phone)
#             # 获取用户的购物车
#             cart = Cart.objects.get(user=user)
#             # 创建序列化器
#             ser = GetMyCartSerialize(cart)
#             return Response({"status":200,'msg':'获取购物车数据成功','data':ser.data})
#         except User.DoesNotExist:
#             return Response({'status':404,'msg':'用户不存在,找不到购物车'})

class GetCart(generics.GenericAPIView):
    serializer_class = GetMyCartSerialize
    def get_object(self):
        # 获取传递来的token
        token = self.request.headers.get('token')
        payload = decode_jwt(token=token)
        phone = payload.get('phone')
        try:
            # 获取用户并返回对应购物车
            user = User.objects.get(phone=phone)
            cart = Cart.objects.get(user=user)
            return cart
        except User.DoesNotExist:
            raise Http404  # 如果找不到用户，抛出 404 异常

    def get(self, request, *args, **kwargs):
        try:
            # 获取用户购物车对象
            cart = self.get_object()
            # 使用序列化器将购物车数据序列化
            ser = self.get_serializer(cart)
            return Response({"status": 200, 'msg': '获取购物车数据成功', 'data': ser.data})
        except Http404:
            return Response({'status': 404, 'msg': '用户不存在,找不到购物车'})
class CreateCart(generics.ListCreateAPIView):
    """专门处理购物车商品新增"""
    serializer_class = CartItemUpdateSerializer
    queryset = CartItem.objects.all()
    def create(self, request, *args, **kwargs):
        try:
            # 从请求头获取 token
            token = request.headers.get('token')
            if not token:
                raise ValueError("未提供 Token")
            
            # 解码 Token
            payload = decode_jwt(token)
            phone = payload.get('phone')
            
            if not phone:
                raise ValueError("Token 中未找到 phone")
            
            # 获取用户
            try:
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                raise ValueError('用户不存在')

            return super().create(request, *args, **kwargs)
            
        except ValueError as ve:
            return Response(
                {"error": f"Token 验证失败: {str(ve)}"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            return Response(
                {"error": f"未知错误: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class UpdateCart(generics.RetrieveUpdateDestroyAPIView):
    """处理购物车商品的修改/删除"""
    serializer_class = CartItemUpdateSerializer
    queryset = CartItem.objects.all()
    def update(self, request, *args, **kwargs):
        try:
            # 从请求头获取 token
            token = request.headers.get('token')
            if not token:
                raise ValueError("未提供 Token")
            
            # 解码 Token
            payload = decode_jwt(token)
            phone = payload.get('phone')
            if not phone:
                raise ValueError("Token 中未找到 phone")
            
            # 获取用户
            try:
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                raise ValueError('用户不存在')

            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({'error':f'未知错误:{str(e)}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
