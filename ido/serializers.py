from rest_framework import  serializers
from .models import liveData,memberData,historicalRecord,covidRecord,Notice,Lost_Found,Complain

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


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class Lost_FoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost_Found
        fields = '__all__'

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'
