from .models import batch
# from .models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class batchforms(forms.ModelForm):
    class Meta:
        model=batch
        fields=['batchno','module','time','labno']
class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','email','password1','password2']
# class feedbackform(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields =['username','created_date','feedback']

