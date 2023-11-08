from django.db import models
# Create your models here.
from django.db import models


class User(models.Model):
    telephone = models.CharField(max_length=11)
    nickname = models.CharField(max_length=30)


class Oder(models.Model):
    # nickname = models.CharField(max_length=50, verbose_name='昵称')
    telephone = models.CharField(max_length=50, verbose_name='联系电话')
    car_number = models.CharField(max_length=50, verbose_name='车牌号')
    appointment_date = models.CharField(max_length=50, verbose_name='预计年审日期')
    appointment_time = models.CharField(max_length=50, verbose_name='预计车检时间')
    visit = models.CharField(max_length=20, verbose_name='是否上门接车')
    address = models.CharField(max_length=200, verbose_name='接车地点')
    # status = CharField(max_length=8, verbose_name="处理状态")
    type_choices = (
        (0, '未处理'),
        (1, '已处理'),
    )
    type = models.IntegerField(verbose_name='处理状态',default=0,choices=type_choices)

    class Meta:
        verbose_name = "预约信息管理"
        verbose_name_plural = "预约信息管理"

    def __str__(self):
        return self.telephone
