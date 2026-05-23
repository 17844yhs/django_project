from django.urls import path
from banner_app import views
urlpatterns = [
    path('all/',views.GetBannerView.as_view())
]