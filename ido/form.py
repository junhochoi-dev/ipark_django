from django.forms import ModelForm
from django import forms
from django.forms import ClearableFileInput

from .models import memberData
import re
class UploadFileForm(forms.ModelForm):
    # class Meta:
    #     model =memberData
    #     fields=('image',)
    class Meta:
        model = memberData
        fields = ('image',)
        widgets = {
            'image': ClearableFileInput(attrs={"multiple": True}),
        }

