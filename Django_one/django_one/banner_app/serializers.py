from rest_framework import serializers
from .models import Banner

class GetBannerSerailize(serializers.ModelSerializer):

    class Meta:
        model = Banner  # 使用Cart模型而非CartItem
        fields = '__all__'
