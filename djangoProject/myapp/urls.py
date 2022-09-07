"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from myapp import views

urlpatterns = [
    path('NewFile/', views.NewFile),  # 登入前旅遊網
    path('Register/', views.Register),  # 註冊畫面
    path('login/', views.login),  # 存進資料庫
    path('loginsuccess/', views.loginsuccess),  # 登入判別
    path('login_failed/', views.login_failed),  # 登入失敗
    path('front_page/', views.front_page),  # 登入後首頁
    path('newtab/', views.newtab),  # q爬蟲資料
    path('newweb/',views.newweb),
]
