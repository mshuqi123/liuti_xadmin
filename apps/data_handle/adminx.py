import xadmin
# from xadmin.models import ArticleDetail
from xadmin import views
from xadmin.models import UserWidget
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
from data_handle.models import Emmagee
from django.utils.safestring import mark_safe
# Register your models here.

class EmmageeAdmin(object):
    list_display = ['title','files','create_time','update_time', '生成报表','查看报表']
    search_fields = ['title']  # 搜索栏
    list_filter = ['update_time']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-github'
    def 生成报表(self, obj):
        button = '<p id="{0}" class="default btn btn-primary hide-xs" onclick="click_memory_info(\'{1}\')">内存报表</p> ' \
                 '<p id="{2}" class="default btn btn-primary hide-xs" onclick="click_cpu_info(\'{3}\')">cpu报表</p> '.format(obj.id, str(obj.files).split("/")[1],obj.id, str(obj.files).split("/")[1])
        r = mark_safe(button)
        return r

    def 查看报表(self, obj):
        button2 = '<a id="%d" class="default btn btn-primary hide-xs" href="http://129.28.161.243/liuti_box/liuti_box/static/report/memory/%s.html">内存报表</a>' \
                  '&nbsp<a id="%d" class="default btn btn-primary hide-xs" href="http://129.28.161.243/liuti_box/liuti_box/static/report/cpu/%s.html">cpu报表</a>' % (obj.id,str(obj.files).split("/")[1].split(".")[0],obj.id,str(obj.files).split("/")[1].split(".")[0])
        r2 = mark_safe(button2)
        return r2

    def get_media(self):
        media = super(EmmageeAdmin, self).get_media() + self.vendor('xadmin.page.list.js', 'xadmin.page.form.js')
        media += self.vendor('xadmin.list.box.js', 'xadmin.form.css')
        return media
xadmin.site.register(Emmagee,EmmageeAdmin)
