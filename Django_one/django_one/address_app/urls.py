from django.urls import path
from address_app import views
urlpatterns = [
    path('all/',views.GetAddressView.as_view()),
    path('add/',views.AddAddressView.as_view()),
]