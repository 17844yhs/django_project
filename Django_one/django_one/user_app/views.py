from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
# from django.views import View
# from django.http import HttpResponse

from .models import User
from .serializers import RegisterSerialize,UserDetailSerailize
from utils.captcha import *
from utils.pyjwt import encode_jwt,decode_jwt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics

# Create your views here.

def index(request):
    return render(request,'hello.html')

def captcha_img(request):
  '''
   返回验证码
   '''
  # 获取验证码图片和验证码内容
  img,code = generate_captcha()
  # 将验证码内容保存到session中,用于校验
  request.session['code'] = code
  request.session.save()  # 显式保存 session
  # 将图片返回给浏览器
  # 创建一个流文件BaseIo
  stream = BytesIO()
  # 将图片保存到流文件中
  img.save(stream,'png')
  stream.seek(0)
  # 返回数据
  return HttpResponse(stream.getvalue(), content_type='image/png')

class Login(APIView):
    def post(self,request):
        '''
        登录功能
        '''
        # 1.获取验证码
        code = request.data['code']
        # if code.lower() == request.session.get('code', '').lower():
        if code.lower() == '1234':
            # 验证码使用一次就失效
            request.session['code'] = ''
            # 2.根据参数获取用户
            phone = request.data['phone']
            pwd = request.data['pwd']
            user = user = User.objects.get(phone=phone)
            # user = User.objects.filter(phone=phone).first()
            if not user:
                return Response({'msg':'用户不存在','status':404,'nick_name':user.nick_name,'user_id':user.id},)
            # 3.检查密码
            if user.check_pwd(pwd):
                payload = {
                    "phone":phone,
                    "pwd":pwd,
                    "sercet":"1234"
                }
                token = encode_jwt(payload=payload)
                return Response({'msg':'登录成功','status':200,'user_id':user.id,'token':token},status=status.HTTP_200_OK)
            else:
                # return Response({'msg':'密码错误'},status=status.HTTP_400_BAD_REQUEST)
                return Response({'msg':'密码错误','status':400})
        else:
            return Response({'msg':'验证码错误','status':400})

class Register(APIView):
    def post(self,request):
        """
        注册功能
        """
        # 创建序列化器
        serialize = RegisterSerialize(data = request.data)
        # 验证通过
        if serialize.is_valid():
            # 保存数据
            serialize.save()
            return Response({'msg':'注册成功','status':200},status=status.HTTP_200_OK)
        else:
            return Response({'msg':f"注册失败{serialize.errors},'status':400"})

class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserDetailSerailize

    def get(self, request, *args, **kwargs):
        # 1. 从请求头获取 Token
        token = request.headers.get('token')
        if not token:
            return Response(
                {"error": "未提供 Token"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

        # 2. 验证 Token
        try:
            payload = decode_jwt(token)  # 调用你的解码方法
            phone = payload.get('phone')

            if not phone:
                raise ValueError("Token 中未找到 phone")

            try:
                # 通过 phone 获取用户
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                raise ValueError("Token 无效, 找不到对应用户")
            user_id_from_url = kwargs.get('pk') 
            user2 = User.objects.get(id=user_id_from_url)
            if user == user2:
                # 3. 正常返回用户数据
                return super().get(request, *args, **kwargs)
            else:
                return Response(
                {"status":404,'msg':'token和用户id不一致'}
            )

        except Exception as e:
            return Response(
                {"error": f"Token 验证失败: {str(e)}"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )