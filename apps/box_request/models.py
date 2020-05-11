from django.db import models

# Create your models here.

class Param(models.Model):
    '''参数及参数值'''
    query = models.CharField(max_length=1000, verbose_name="参数", default="")
    value = models.CharField(max_length=1000, verbose_name="参数值", default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'box_param'
        verbose_name = "参数异常"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.query

class Requests(models.Model):
    '''请求'''
    name = models.CharField(max_length=100, verbose_name="用例名称", default="")
    state_choices = (
        (u'J', u'禁用'),
        (u'Q', u'启用'),
    )
    state = models.CharField(max_length=10,
                              choices=state_choices,
                              verbose_name="状态",
                              default="J")
    host = models.CharField(max_length=100, verbose_name="过滤服务器",blank=True, null=True,default="")
    path = models.CharField(max_length=100, verbose_name="过滤接口",blank=True, null=True,default="")
    hosta = models.CharField(max_length=100, verbose_name="all服务器",blank=True, null=True,default="")
    hostd = models.CharField(max_length=100, verbose_name="单个服务器",blank=True, null=True,default="")
    paths = models.CharField(max_length=100, verbose_name="异常接口路径",blank=True, null=True,default="")
    hosty = models.CharField(max_length=100, verbose_name="异常服务器",blank=True, null=True,default="")
    query = models.ManyToManyField(Param, verbose_name="参数", blank=True, null=True, default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'box_request'
        verbose_name = "异常请求"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Response(models.Model):
    '''返回'''
    fname = models.CharField(max_length=100, verbose_name="用例名称", default="")
    state_choices = (
        (u'J', u'禁用'),
        (u'Q', u'启用'),
    )
    state = models.CharField(max_length=10,
                             choices=state_choices,
                             verbose_name="状态",
                             default="J")
    old = models.CharField(max_length=100, verbose_name="正常返回数据",blank=True, null=True,default="")
    new = models.CharField(max_length=100, verbose_name="模拟异常数据",blank=True, null=True,default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'box_response'
        verbose_name = "异常返回"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.fname

class Http_connect(models.Model):
    '''整体返回异常'''
    yname = models.CharField(max_length=100, verbose_name="用例名称", default="")
    state_choices = (
        (u'J', u'禁用'),
        (u'Q', u'启用'),
    )
    state = models.CharField(max_length=10,
                             choices=state_choices,
                             verbose_name="状态",
                             default="J")
    hosts = models.CharField(max_length=100, verbose_name="all服务器",blank=True, null=True,default="")
    host = models.CharField(max_length=100, verbose_name="单个服务器",blank=True, null=True,default="")
    path = models.CharField(max_length=100, verbose_name="异常接口",blank=True, null=True,default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'box_http_connect'
        verbose_name = "整体异常"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.yname
class Api_path(models.Model):
    '''接口路径列表'''
    name = models.CharField(max_length=100, verbose_name="接口名称" , unique=True, default="")
    id = models.IntegerField(verbose_name="接口编号", unique=True, default="")
    path = models.CharField(max_length=100, primary_key=True, verbose_name="接口路径", default="")
    state_choices = (
        (u'J', u'禁用'),
        (u'Q', u'启用'),
    )
    state = models.CharField(max_length=10,
                             choices=state_choices,
                             verbose_name="状态",
                             default="J")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'box_api_path'
        verbose_name = "接口列表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.path
class Get_time(models.Model):
    '''接口响应时间列表'''
    name = models.CharField(max_length=100, verbose_name="接口名称", blank=True, null=True, default="")
    path = models.CharField(max_length=100, verbose_name="接口路径", default="")
    xtime = models.FloatField(default="", verbose_name='响应时间')
    get_time = models.CharField(max_length=100, verbose_name="请求时间", blank=True, null=True, default="")
    class Meta:
        db_table = 'box_get_time'
        verbose_name = "响应时间"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.path

















