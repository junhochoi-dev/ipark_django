from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import liveData,memberData,historicalRecord,covidRecord
from rest_framework import viewsets
from .serializers import liveDataSerializer,covidRecordSerializer,memberDataSerializer,historicalRecordSerializer


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