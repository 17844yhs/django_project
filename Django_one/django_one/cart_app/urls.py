from django.urls import path
from cart_app import views
urlpatterns = [
    path('category/',views.GetCategory.as_view()),
    path('goodsbycategory/',views.GetGoodsBycategory.as_view()),
    path('goodsbyname/',views.GetGoodsByName.as_view()),
    path('cart/',views.GetCart.as_view()),
    path('cart/item/create/',views.CreateCart.as_view()),
    path('cart/item/update/<int:pk>',views.UpdateCart.as_view()),
    path('cart/item/delete/<int:pk>',views.UpdateCart.as_view()),
]