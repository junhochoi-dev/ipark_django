from django.db import models
from datetime import datetime,timedelta
from django.utils.dateformat import DateFormat
from dateutil.relativedelta import relativedelta
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class liveData(models.Model):
    name = models.CharField(max_length=40 ,blank=True,default = '', null=True )              # 이름
    major = models.CharField(max_length=40,blank=True,default = '', null=True )              #학과
    student_num = models.CharField(max_length=50)                                           # 학번
    phone_num = models.CharField(default = '',max_length=50, primary_key=True)              #번호-primary
    enter_time = models.CharField(null=True,default='',max_length=50)  # 입장시간
    reserve_product =  models.CharField(max_length=10,default = '')   # 예약상품
    objects = models.Manager() # ~has no member vscode 에러 해결코드

    def __str__(self):
        return str(self.name) if self.name else ''


class memberData(models.Model): # 이번달 사용자 DB (액셀에서 받아온거) ##field는 import를 위해 늘림
    num = models.CharField(max_length=100000,default = '',help_text='순번 ex)3월 아침 1번째, 3월 종일 1번째')              # 순번

    graduate_status = (

        ( '학부생', '학부생'),
        ('대학원생', '대학원생'),
        ( '교직원', '교직원'),
        )

    graduate = models.CharField(max_length=20,choices=graduate_status)          # 대학원/학부
    major = models.CharField(max_length=40,default = '')              # 학과
    student_num = models.CharField(max_length=20,default = '')        # 학번
    name = models.CharField(max_length=40,default = '')               # 이름
    email = models.CharField(default = '',max_length=128, primary_key=True,help_text='꼭 학교 이메일만  사용하고  ***@korea 까지만 저장해주세요!!!')             # 이메일-primary
    phone_num = models.CharField(max_length=15,default = '',null=True)          # 번호

    # reserve_status = (
    #     (datetime.now().strftime('%-m')+'월 종일', datetime.now().strftime('%-m')+'월 종일'),
    #     (datetime.now().strftime('%-m')+'월 아침', datetime.now().strftime('%-m')+'월 아침'),
    #     ((datetime.now()+relativedelta(months=1)).strftime('%m')+'월 종일',(datetime.now()+relativedelta(months=1)).strftime('%m')+'월 종일'),
    #     ((datetime.now()+relativedelta(months=1)).strftime('%m')+'월 아침',(datetime.now()+relativedelta(months=1)).strftime('%m')+'월 아침'),
    #     ('1학기 종일', '1학기 종일'),
    #     ('1학기 아침', '1학기 아침'),
    #     ('2학기 종일', '2학기 종일'),
    #     ('2학기 아침', '2학기 아침'),

    #     )

    # reserve_product =  models.CharField(max_length=100,choices=reserve_status)   # 예약상품

    reserve_product =  models.CharField(max_length=100,default = '')   # 예약상품

    price_status = (
        ('12', '120,000'),
        ('4', '40,000'),
        ('3', '30,000'),
        ('1', '10,000'),
        )

    price = models.CharField(max_length=20,choices=price_status)              #120000/30000

    objects = models.Manager()


class historicalRecord(models.Model): # 과거사용자 DB
    name = models.CharField(max_length=40,default = '')               # 이름
    major = models.CharField(max_length=40,default = '')              # 학과
    student_num = models.CharField(max_length=20,default = '')        # 학번
    phone_num = models.CharField(max_length=15,default = '',primary_key=True)     # 번호-primary
    reserve_product =  models.CharField(max_length=20,default = '')   # 예약상품
    email = models.CharField(max_length=128,default = '') # 이메일

    objects = models.Manager()

class covidRecord(models.Model): # 코로나 추적 DB & graph show function & auto remove every two weeks
    name = models.CharField(max_length=40,default = '')               # 이름
    major = models.CharField(max_length=40,default = '')              # 학과
    student_num = models.CharField(max_length=20,default = '')        # 학번
    phone_num = models.CharField(max_length=15,default = '')         # 번호-primary
    enter_time = models.CharField(default='',max_length=50)  # 입장시간
    id  = models.AutoField(primary_key=True)

    objects = models.Manager()




