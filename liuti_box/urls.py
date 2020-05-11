"""liuti_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from liuti_box import settings
from django.views.static import serve
import xadmin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^box_request/', include(('box_request.urls','box_request'), namespace='box_request')),  # 异常请求模块
    url(r'^data_handle/', include(('data_handle.urls','data_handle'), namespace='data_handle')),  # 数据处理模块
]
