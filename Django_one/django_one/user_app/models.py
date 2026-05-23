import hashlib
from django.db import models

# Create your models here.
class User(models.Model):
    choice = ((1,'男'),(0,'女'))
    phone = models.CharField(null=True,blank=True,max_length=11,verbose_name='手机号')
    nick_name = models.CharField(max_length=18,null=True,blank=True,default='系统昵称',verbose_name='用户昵称')
    pwd = models.CharField(max_length=32,null=True,blank=True,verbose_name='密码')
    _pwd = models.CharField(max_length=32,null=True,blank=True,verbose_name='真实密码')
    gender = models.IntegerField(choices=choice,default=1,verbose_name='性别')
    introduction = models.TextField(null=True,blank=True,default='该用户很懒,什么介绍都没有',verbose_name='用户简介')
    avatar = models.CharField(null=True,blank=True,max_length=50,verbose_name='头像')

    create_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')
    class Meta:
        db_table= 't_user'
    @property
    def pwd(self):
        return self._pwd
    @pwd.setter # 上面的
    def pwd(self,pwd):
        self._pwd = hashlib.md5(pwd.encode()).hexdigest()
    
    def check_pwd(self,raw_pwd):
        encrypted = hashlib.md5(raw_pwd.encode()).hexdigest()
        return encrypted == self.pwd