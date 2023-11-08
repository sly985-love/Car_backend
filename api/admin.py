# from django.contrib import admin
# from django.db.models import Sum
# from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
# from django.contrib import admin
# from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Oder
# 在此添加站点
# Register your models here.
admin.site.site_header = '车检预约员工管理后台'
admin.site.site_title = '车检预约员工管理后台'
admin.site.index_title = '车检预约员工管理后台'


# class oder(admin.ModelAdmin):
#     list_display = ('telephone', 'car_number', 'appointment_date', 'appointment_time', 'visit', 'address', 'type')
#     search_fields = ('telephone', 'car_number', 'appointment_date', 'appointment_time', 'visit', 'address', 'type')
#     list_filter = ('telephone', 'car_number', 'appointment_date', 'appointment_time', 'visit', 'address', 'type')
#
#
# admin.site.register(Oder, oder)

class ProxyResource(resources.ModelResource):
    class Meta:
        model = Oder

# Register your models here.
@admin.register(Oder)
# # class RecordAdmin(admin.ModelAdmin):
# # class RecordAdmin(ImportExportModelAdmin):
# # class RecordAdmin(ImportExportActionModelAdmin):
class RecordAdmin(ExportActionModelAdmin):
    resource_class = ProxyResource

    list_display = ('telephone', 'car_number', 'appointment_date', 'appointment_time', 'visit', 'address', 'type')
    search_fields = ('telephone', 'car_number', 'appointment_date', 'appointment_time', 'visit', 'address', 'type')
    list_filter = ('telephone', 'car_number', 'appointment_date', 'appointment_time', 'visit', 'address', 'type')
    list_per_page = 10

    actions = ('custom_btn',)

    def custom_btn(self,request,queryset):
        pass

    custom_btn.short_description = '测试按钮'
