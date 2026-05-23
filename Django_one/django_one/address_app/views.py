from rest_framework.views import APIView
from rest_framework.response import Response
from utils.pyjwt import decode_jwt
from .serializers import GetAddressSerailizer,AddressSerializer
from .models import AddressModel
from user_app.models import User
# Create your views here.
class GetAddressView(APIView):
    def get(self,request):
        token = request.headers.get('token')
        if not token:
            return Response({'status':400,'msg':"缺少token"})
        try:
            payload = decode_jwt(token)
            phone = payload.get('phone')
            user = User.objects.get(phone=phone)
            # 获取所有address
            address = AddressModel.objects.all()
            # 获取序列化器
            ser = GetAddressSerailizer(address,many=True)
            return Response({'data':ser.data,'status':200,'msg':'获取地址成功'})
        except User.DoesNotExist:
            return Response({'status':404,'msg':'查无此用户'})
        except Exception as e:
            return Response({'status':500,'msg':'获取地址失败'})

class AddAddressView(APIView):
    def post(self,request):
        token = request.headers.get('token')
        if not token:
            return Response({'status':400,'msg':'缺少token'})
        try:
            data= request.data
            # 获取序列化器
            ser = AddressSerializer(data=data)
            if ser.is_valid():
                ser.save() #保存到数据库
                return Response({'status':200,'msg':'增加地址成功'})
            return Response({'status':401,'msg':'用户验证失败'})
        except Exception as e:
            return Response({'status':500,'msg':'增加地址失败'})