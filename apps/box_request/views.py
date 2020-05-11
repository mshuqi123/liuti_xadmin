from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from box_request.models import Requests,Response,Http_connect,Api_path,Get_time
from django.db import connection
from django.core import serializers
import requests,os,time
from pyecharts import *
from liuti_box import settings
import logging
log = logging.getLogger("django")
# Create your views here.

def get_request(request):
    data = {}
    param = {}
    results = Requests.objects.filter(state='Q').order_by("-update_time").values()
    query = Requests.objects.filter(state='Q').order_by("-update_time").first()
    if results:
        results1 = query.query.all().values()
        param['query'] = list(results1)
        data['code'] = 200
        data["data"] = list(results)[0]
        data["param"] = param
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def get_response(request):
    data = {}
    results = Response.objects.filter(state='Q').order_by("-update_time").values()
    log.info(list(results))
    if results:
        data['code'] = 200
        data["data"] = list(results)[0]
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def http_connect(request):
    data = {}
    results = Http_connect.objects.filter(state='Q').order_by("-update_time").values()
    if results:
        data['code'] = 200
        data["data"] = list(results)[0]
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def get_apipath(request):
    data = {}
    results = Api_path.objects.filter(state='Q').values()
    if results:
        data['code'] = 200
        data["data"] = list(results)
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def get_time(request):
    data = {}
    results = Get_time.objects.all().values()
    if results:
        data['code'] = 200
        data["data"] = list(results)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def get_boxapitime(request):
    pid = request.GET.get('id',)
    try:
        url = Api_path.objects.filter(id=pid).values()
        tpath = list(url)[0]["path"]
        zdata = []
        xtime = Get_time.objects.filter(path=tpath).order_by("get_time").values()
        if xtime:
            data = []
            for i in xtime:
                p = i["xtime"]
                data.append(p)
            if len(data) != 0:
                zdata.append(data)
            performance_data = os.path.join(settings.BASE_DIR, 'static/report')
            html_path = "%s/%s.html" % (performance_data, pid)
            title = "闪电盒子-编号%s号接口响应时间报表" %pid
            case_list = []
            for r in zdata:
                for z in range(len(r)):
                    case_list.append(z)
                bar = Line(title, "图表纵轴为响应时间数据大小，横轴为接口请求时间得正序编号，直线为平均值")
                bar.add("time (单位：秒）", case_list, r, label_color=['#B22222'], mark_line=["average"],
                            mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
                bar.use_theme("vintage")
                bar.render(html_path)
            return JsonResponse({'code': 200, 'message': '生成报表成功'})
        else:
            return JsonResponse({'code': 404, 'message': '该接口暂时无数据，不可生成成报表'})
    except 	IndexError:
        return JsonResponse({'code': 404, 'message': '参数错误，没有该编号的接口'})














