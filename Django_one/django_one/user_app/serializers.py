from rest_framework import serializers
from .models import User


class RegisterSerialize(serializers.ModelSerializer):
    phone = serializers.CharField(
        max_length=11,
        min_length=11,
        required=True,
    )
    nick_name = serializers.CharField(max_length=18,allow_blank=True,trim_whitespace=True,required=False)
    pwd = serializers.CharField(max_length=32,allow_blank=True,required=True)
    gender = serializers.IntegerField(min_value=0,max_value=1,required=False)
    introduction = serializers.CharField(required=False)
    avatar = serializers.CharField(required=False)


    def validate_phone(self, value):
        user = User.objects.filter(phone=value).exists()
        if user:
            raise serializers.ValidationError('手机号已经注册')
        return value

    class Meta:
        model = User
        fields = '__all__'

class UserDetailSerailize(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('create_at','update_at','_pwd')