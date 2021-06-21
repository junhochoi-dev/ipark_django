from rest_framework import  serializers
from .models import liveData,memberData,historicalRecord,covidRecord

class liveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = liveData
        fields = '__all__'

class memberDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberData
        fields = '__all__'

class historicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = historicalRecord
        fields = '__all__'


class covidRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = covidRecord
        fields = '__all__'
