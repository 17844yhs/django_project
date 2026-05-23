from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GetBannerSerailize
from .models import Banner
# Create your views here.
class GetBannerView(APIView):
    def get(self,request):
        try:
            # 获取所有bannermodel
            banners = Banner.objects.all()
            # 获取序列化器
            ser = GetBannerSerailize(banners,many=True)
            
            return Response({'data':ser.data,'status':200,'msg':'获取轮播图成功'})
        except BaseException as e:
            return Response({'status':500,'msg':'获取轮播图失败'})