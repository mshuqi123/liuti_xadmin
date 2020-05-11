from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from data_handle.models import Emmagee
from django.db import connection
from django.core import serializers
import requests,os,time
from pyecharts import *
from liuti_box import settings
# Create your views here.

def get_memory(request):
    # 处理内存数据并生成报表
    name = request.GET.get('filename',)
    pid = "emmagee/" + str(name)
    try:
        url = Emmagee.objects.filter(files=pid).values()
        data = {}
        if url:
            data["data"] = list(url)
        else:
            return JsonResponse({'code': 404, 'message': '没有找到您要处理的文件'})
        path = data["data"][0]["files"]
        mfile = ('%s' % (settings.MEDIA_ROOT + "/" + path))
        fp = open(mfile, encoding='gbk', mode='r')
        list_lines = fp.readlines()
        fp.close()
        than = []
        pss = []
        mem = []
        for l in list_lines[9:]:
            pss.append(l.split(",")[2])
            than.append(l.split(",")[3])
            mem.append(l.split(",")[4])
        id = []
        for i in range(len(list_lines[9:])):
            id.append(i)
        performance_data = os.path.join(settings.BASE_DIR, 'static/report')
        name = str(path).split("/")[1].split(".")[0]
        html_path = "%s/memory/%s.html" % (performance_data,name)
        bar = Line("闪电盒子__内存数据图形报表", "图表纵轴为数据大小，横轴为时间节点，直线为平均值")
        bar.add("占用内存", id, pss, label_color=['#800080'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.add("总内存", id, mem, label_color=['#0000FF'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.add("占用比例", id, than, label_color=['#2E8B57'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.use_theme("vintage")
        bar.render(html_path)
        return JsonResponse({'code': 200, 'message': '生成内存数据处理报表成功'})
    except 	IndexError:
        return JsonResponse({'code': 404, 'message': '参数错误，没有该文件'})

def get_cpu(request):
    # 处理cpu数据并生成报表
    name = request.GET.get('filename', )
    pid = "emmagee/" + str(name)
    try:
        url = Emmagee.objects.filter(files=pid).values()
        data = {}
        if url:
            data["data"] = list(url)
        else:
            return JsonResponse({'code': 404, 'message': '没有找到您要处理的文件'})
        path = data["data"][0]["files"]
        mfile = ('%s' % (settings.MEDIA_ROOT + "/" + path))
        fp = open(mfile, encoding='gbk', mode='r')
        list_lines = fp.readlines()
        fp.close()
        cpu = []
        zcpu = []
        for l in list_lines[9:]:
            cpu.append(l.split(",")[5])
            zcpu.append(l.split(",")[6])
        id = []
        for i in range(len(list_lines[9:])):
            id.append(i)
        performance_data = os.path.join(settings.BASE_DIR, 'static/report')
        name = str(path).split("/")[1].split(".")[0]
        html_path = "%s/cpu/%s.html" % (performance_data,name)
        bar = Line("闪电盒子__CPU数据图形报表", "图表纵轴为数据大小，横轴为时间节点，直线为平均值")
        bar.add("占用CPU率", id, cpu, label_color=['#800080'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.add("CPU总使用率", id, zcpu, label_color=['#0000FF'], mark_line=["average"],
                mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
        bar.use_theme("vintage")
        bar.render(html_path)
        return JsonResponse({'code': 200, 'message': '生成cpu数据处理报表成功'})
    except 	IndexError:
        return JsonResponse({'code': 404, 'message': '参数错误，没有该文件'})












