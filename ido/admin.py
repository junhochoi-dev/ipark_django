from django.contrib import admin
from .models import liveData,memberData,historicalRecord,covidRecord
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
import datetime
from django.db import IntegrityError


class liveDataCustom(admin.ModelAdmin):
    list_display = ['name', 'major', 'student_num', 'reserve_product', 'enter_time']
    ordering = ['enter_time']
    list_filter = ['name']
    search_fields = ['name', 'major', 'student_num', 'phone_num', 'reserve_product']


class memberDataCustom(ImportExportMixin, admin.ModelAdmin):
  

    list_display = ['name', 'major', 'student_num', 'phone_num', 'reserve_product', 'email']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name', 'major', 'student_num', 'phone_num', 'reserve_product', 'email']
    actions = ['move_to_Live']  # move_to_Live
    
    ## import 수정중
    #exclude = ['id']
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    import_id_fields=('name', 'major', 'student_num', 'phone_num', 'reserve_product', 'email')
## import 수정중   

    def move_to_Live(self, request, queryset):  #

        qs = queryset.values()  # 체크박스로 입력된 쿼리값들 받아옴
        a = qs[0]['name']
        for q in range(len(qs)):
            now = datetime.datetime.now()  # 현재시간
            nowDatetime = now.strftime('%Y/%m/%d %H:%M:%S')
            try:
                liveData.objects.get_or_create(name=qs[q]['name'], major=qs[q]['major'],
                                               student_num=qs[q]['student_num'], phone_num=qs[q]['phone_num'],
                                               enter_time=nowDatetime ,
                                               reserve_product=qs[q]['reserve_product'])  # liveData에 넣기
                covidRecord.objects.get_or_create(name=qs[q]['name'], major=qs[q]['major'],
                                               student_num=qs[q]['student_num'], phone_num=qs[q]['phone_num'],
                                               enter_time=nowDatetime)  # liveData에 넣기
                self.message_user(request, "등록완료!{}".format(qs[q]))  # django message framework 사용
            except IntegrityError as e:
                if 'UNIQUE constraint' in str(e.args):
                    self.message_user(request,"이미 등록된 회원입니다{}".format(qs[q]))  # django message framework 사용

    move_to_Live.short_description = '실시간 인원에 등록합니다'



class historicalRecordCustom(admin.ModelAdmin):
    list_display = ['name','major','student_num','reserve_product','email']
    ordering = ['reserve_product']
    list_filter = ['name']
    search_fields =['name']

class covidRecordCustom(admin.ModelAdmin):
    list_display = ['name','major','phone_num', 'enter_time']
    ordering = ['-enter_time']
    list_filter = ['name']
    search_fields =['name','student_num']



admin.site.register(liveData,liveDataCustom)
admin.site.register(memberData,memberDataCustom)
admin.site.register(historicalRecord,historicalRecordCustom)
admin.site.register(covidRecord,covidRecordCustom)

