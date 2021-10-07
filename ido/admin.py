from django.contrib import admin
from .models import liveData,memberData,historicalRecord,covidRecord
from import_export.admin import ImportExportMixin, ImportMixin
import datetime

from django.db import IntegrityError
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.db.models import Value
from django.db.models.functions import Replace

class liveDataCustom(admin.ModelAdmin):
    list_display = ['name', 'major', 'student_num', 'reserve_product', 'enter_time']
    ordering = ['enter_time']
    #list_filter = ['name']
    search_fields = ['name', 'major', 'student_num', 'phone_num', 'reserve_product']



class MemberResource(resources.ModelResource):

    # def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     headers = ['num','graduate','major','student_num','name','email','phone_num','reserve_product','price']
    #     dataset.headers = headers

    def before_import_row(self, row, **kwargs):
        row['email'] = row['email'].replace('.ac.kr','')

    class Meta:
        model = memberData
        #fields =('num','graduate','major','student_num','name','email','phone_num','reserve_product','price')
        #exclude = ('name',)
        #exclude = ('num',)
        import_id_fields = ('email',)
        #resources.ModelResource.get_queryset().objects.update(email=Replace('email', Value('.ac.kr'), Value('')))



class memberDataCustom(ImportExportMixin, admin.ModelAdmin):

    resource_class=MemberResource
    #self.get_queryset().objects.update(email=Replace('email', Value('.ac.kr'), Value('')))
    #memberData.objects.update(email=Replace('email', Value('.ac.kr'), Value('')))
    list_display = ['name', 'major', 'student_num', 'phone_num', 'reserve_product', 'email']
    ordering = ['name']
    #list_filter = ['name']
    search_fields = ['name', 'major', 'student_num', 'phone_num', 'reserve_product', 'email']
    actions = ['move_to_Live']  # move_to_Live


    list_max_show_all = 5000
    list_per_page = 100

    def move_to_Live(self, request, queryset):  #

        qs = queryset.values()  # 체크박스로 입력된 쿼리값들 받아옴

        for q in range(len(qs)):
            now = datetime.datetime.now()  # 현재시간
            nowDatetime = now.strftime('%Y/%m/%d %H:%M:%S')
            try:
                liveData.objects.get_or_create(name=qs[q]['name'], major=qs[q]['major'],
                                               student_num=qs[q]['student_num'], phone_num=qs[q]['phone_num'],
                                               enter_time=nowDatetime,
                                               reserve_product=qs[q]['reserve_product'])  # liveData에 넣기

                covidRecord.objects.get_or_create(name=qs[q]['name'], major=qs[q]['major'],
                                               student_num=qs[q]['student_num'], phone_num=qs[q]['phone_num'],
                                               enter_time=nowDatetime)  # liveData에 넣기
                self.message_user(request, "등록완료!{}".format(qs[q]))  # django message framework 사용
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    self.message_user(request,"이미 등록된 회원입니다{}".format(qs[q]))  # django message framework 사용

    move_to_Live.short_description = '실시간 인원에 등록합니다'



# class historicalRecordCustom(admin.ModelAdmin):
#     list_display = ['name','major','student_num','reserve_product','email']
#     ordering = ['reserve_product']
#     #list_filter = ['name']
#     search_fields =['name']

class covidRecordCustom(admin.ModelAdmin):
    list_display = ['name','major','phone_num', 'enter_time','id']
    ordering = ['-enter_time']
    #list_filter = ['name']
    search_fields =['name','student_num']



admin.site.register(liveData,liveDataCustom)
admin.site.register(memberData,memberDataCustom)
#admin.site.register(historicalRecord,historicalRecordCustom)
admin.site.register(covidRecord,covidRecordCustom)

