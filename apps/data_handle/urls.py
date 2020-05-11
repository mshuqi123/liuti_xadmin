from django.conf.urls import url
from apps.data_handle import views
# app_name = 'box_request'
urlpatterns = [
    url(r'^memory', views.get_memory, name='memmory'),    # 处理内存数据
    url(r'^cpu', views.get_cpu, name='cpu'),    # 处理cpu数据
]
