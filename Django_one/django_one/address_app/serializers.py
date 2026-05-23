from rest_framework import serializers
from .models import AddressModel

class GetAddressSerailizer(serializers.ModelSerializer):
    class Meta:
        model =  AddressModel
        fields = '__all__'

from rest_framework import serializers
from .models import AddressModel

class AddressSerializer(serializers.ModelSerializer):
    # 这里你可以自定义字段验证
    class Meta:
        model = AddressModel
        fields = ['name', 'phone', 'province', 'city', 'district', 'detail', 'isDefault']

    # 验证电话号码格式（11 位数字）
    def validate_phone(self, value):
        if len(value) != 11 or not value.isdigit():
            raise serializers.ValidationError("电话号码必须是11位数字")
        return value

    # 验证 isDefault 是否为 0 或 1
    def validate_isDefault(self, value):
        if value and value not in [0, 1]:
            raise serializers.ValidationError("地址字段必须为 0或 1")
        return value

    # 验证省、市、区、具体地址是否为空
    def validate(self, data):
        if not data.get('province'):
            raise serializers.ValidationError("省份不能为空")
        if not data.get('city'):
            raise serializers.ValidationError("城市不能为空")
        if not data.get('district'):
            raise serializers.ValidationError("区县不能为空")
        if not data.get('detail'):
            raise serializers.ValidationError("具体地址不能为空")
            
        return data
    
    def create(self, validated_data):
        # 如果新增的地址是默认地址，则先把之前的默认地址设为 0
        if validated_data.get('isDefault') == 1:
            AddressModel.objects.filter(isDefault=1).update(isDefault=0)
        
        return super().create(validated_data)