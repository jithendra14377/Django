from django.urls import path

from .views import account_dashboard,account_home,account_login,account_logout,account_register

urlpatterns=[
    path('home/',account_home,name='account_home'),
    path('dashboard/',account_dashboard,name='account_dashboard'),
    path('register/',account_register,name='account_register'),
    path('login/',account_login,name='account_login'),
    path('logout/',account_logout,name='account_logout')

]