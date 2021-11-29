from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import liveData,memberData,historicalRecord,covidRecord,Notice,Lost_Found,Complain
from rest_framework import viewsets
from .serializers import liveDataSerializer,covidRecordSerializer,memberDataSerializer,historicalRecordSerializer,NoticeSerializer,Lost_FoundSerializer,ComplainSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .form import UploadFileForm



# Create your views here.

class liveDataViewset(viewsets.ModelViewSet):
    queryset = liveData.objects.all()
    serializer_class = liveDataSerializer

class memberDataViewset(viewsets.ModelViewSet):
    queryset = memberData.objects.all()
    serializer_class = memberDataSerializer

class historicalRecordViewset(viewsets.ModelViewSet):
    queryset = historicalRecord.objects.all()
    serializer_class = historicalRecordSerializer

class covidRecordViewset(viewsets.ModelViewSet):
    queryset = covidRecord.objects.all()
    serializer_class = covidRecordSerializer

class covidRecordViewset(viewsets.ModelViewSet):
    queryset = covidRecord.objects.all()
    serializer_class = covidRecordSerializer

class noticeViewset(viewsets.ModelViewSet):
    queryset =Notice.objects.all()
    serializer_class = NoticeSerializer

class lost_foundViewset(viewsets.ModelViewSet):
    queryset=Lost_Found.objects.all()
    serializer_class = Lost_FoundSerializer

class complainViewset(viewsets.ModelViewSet):
    queryset=Complain.objects.all()
    serializer_class = ComplainSerializer


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if form.is_valid():
            for f in files:
                
                email=f.name.split(".")[0]
                try:
                    instance = memberData.objects.get(email=email)
                    instance.image=f
                    instance.save()
                except memberData.DoesNotExist:
                    pass    
                # file_instance = memberData(name=f,email=f,image=f)
                # file_instance.save()
       
            return HttpResponse('upload success')
        else:
            return HttpResponse('bad')
    else:
        form = UploadFileForm()
    return render(request, 'image_upload.html', {'form': form})