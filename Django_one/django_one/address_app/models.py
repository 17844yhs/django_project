from django.db import models

# Create your models here.

class AddressModel(models.Model):
    Choices = [(0,'false'),(1,'true')]

    name = models.CharField(max_length=32,verbose_name='姓名')
    phone = models.CharField(max_length=11,verbose_name='电话号码')
    province = models.CharField(max_length=64,verbose_name='省份')
    city = models.CharField(max_length=32,verbose_name='城市')
    district = models.CharField(max_length=32,verbose_name='区县')
    detail = models.CharField(max_length=32,verbose_name='具体地址')
    isDefault = models.CharField(max_length=8,choices=Choices,verbose_name='默认地址',default=0)

    class Meta:
        db_table = 't_address'
        