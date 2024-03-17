from django import forms
class student_form1(forms.Form):
    roll_no=forms.IntegerField()
    name=forms.CharField(max_length=30)
    email=forms.EmailField()


