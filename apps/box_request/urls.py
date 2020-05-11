from django.conf.urls import url
from apps.box_request import views
# app_name = 'box_request'
urlpatterns = [
    url(r'^request$', views.get_request, name='request'),    # 异常请求
    url(r'^response$', views.get_response, name='response'),    # 异常返回
    url(r'^http_connect$', views.http_connect, name='http_connect'),  # 整体异常返回
    url(r'^get_apipath$', views.get_apipath, name='get_apipath'),  # 接口列表
    url(r'^get_time$', views.get_time, name='get_time'),  # 获取响应时间数据接口
    url(r'^get_boxapitime/', views.get_boxapitime, name='get_boxapitime'),  # 生成接口响应时间报表接口
]
