from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/register/',views.register,name='register'),
    path('accounts/',include('django.contrib.auth.urls')),
]
