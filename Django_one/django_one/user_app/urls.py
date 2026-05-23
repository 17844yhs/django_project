from django.urls import path
from user_app import views

urlpatterns = [
    path("",views.index,name='index'),
    path("captcha/",views.captcha_img,name='code'),
    path("login/",views.Login.as_view(),name='login'),
    path("register/",views.Register.as_view(),name='register'),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]