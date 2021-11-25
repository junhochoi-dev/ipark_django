"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include
from ido.views import memberDataViewset,covidRecordViewset,liveDataViewset,historicalRecordViewset,noticeViewset,lost_foundViewset,complainViewset
from django.conf import settings 
from django.conf.urls.static import static 

admin.autodiscover()
admin.site.enable_nav_sidebar = False
router = routers.DefaultRouter()
router.register('liveData',liveDataViewset)
router.register('historicalRecord',historicalRecordViewset)
router.register('memberData',memberDataViewset)
router.register('covidRecord',covidRecordViewset)
router.register('notice',noticeViewset)
router.register('lost_found',lost_foundViewset)
router.register('complain',complainViewset)
urlpatterns = [
    path('admin/', admin.site.urls,),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
