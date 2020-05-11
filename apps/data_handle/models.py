from django.db import models

# Create your models here.

class Emmagee(models.Model):
    '''参数及参数值'''
    title = models.CharField(max_length=50, verbose_name="文件名称", default="")  # 需要处理的文件名称
    files = models.FileField(verbose_name="文件路径", upload_to="emmagee",unique=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'box_emmagee'
        verbose_name = "Emmagee数据处理"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title