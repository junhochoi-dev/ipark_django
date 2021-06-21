from django.db import models

#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class liveData(models.Model):
    name = models.CharField(max_length=20 ,blank=True,default = '', null=True )              # 이름
    major = models.CharField(max_length=20,blank=True,default = '', null=True )              #학과
    student_num = models.CharField(max_length=50)                                           # 학번
    phone_num = models.CharField(default = '',max_length=50, primary_key=True)              #번호-primary
    enter_time = models.CharField(null=True,default='',max_length=50)  # 입장시간
    reserve_product =  models.CharField(max_length=10,default = '')   # 예약상품
    objects = models.Manager() # ~has no member vscode 에러 해결코드
    
    def __str__(self):
        return str(self.name) if self.name else ''


class memberData(models.Model): # 이번달 사용자 DB (액셀에서 받아온거)
    name = models.CharField(max_length=20,default = '')               # 이름
    major = models.CharField(max_length=20,default = '')              # 학과
    student_num = models.CharField(max_length=20,default = '')        # 학번
    phone_num = models.CharField(max_length=15,default = '',null=True)          # 번호
    reserve_product =  models.CharField(max_length=10,default = '')   # 예약상품
    email = models.CharField(default = '',max_length=128, primary_key=True)             # 이메일-primary

    objects = models.Manager()


class historicalRecord(models.Model): # 과거사용자 DB
    name = models.CharField(max_length=20,default = '')               # 이름
    major = models.CharField(max_length=20,default = '')              # 학과
    student_num = models.CharField(max_length=20,default = '')        # 학번
    phone_num = models.CharField(max_length=15,default = '',primary_key=True)     # 번호-primary
    reserve_product =  models.CharField(max_length=20,default = '')   # 예약상품
    email = models.CharField(max_length=128,default = '') # 이메일
    
    objects = models.Manager()

class covidRecord(models.Model): # 코로나 추적 DB & graph show function & auto remove every two weeks
    name = models.CharField(max_length=20,default = '')               # 이름
    major = models.CharField(max_length=20,default = '')              # 학과
    student_num = models.CharField(max_length=20,default = '')        # 학번
    phone_num = models.CharField(max_length=15,default = '')         # 번호-primary
    enter_time = models.CharField(default='',max_length=50,primary_key=True)  # 입장시간
    what=models      
    objects = models.Manager()




