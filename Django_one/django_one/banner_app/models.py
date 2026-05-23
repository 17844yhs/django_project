from django.db import models

# Create your models here.
class Banner(models.Model):
    pic = models.CharField(max_length=32,verbose_name='轮播图图片地址')
    title = models.CharField(max_length=32,verbose_name='轮播标题')
    class Meta:
        db_table = 't_banner'
