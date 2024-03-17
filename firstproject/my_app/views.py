from django.shortcuts import render
from .models import Stock
from .forms import student_form1
# Create your views here.
def index(request):
    return render(request,'index.html')
def contactus(request):
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')
def product(request):
    st=Stock.objects.all()
    return render(request,'data_task.html',{'Stock':st})
def studentinfo(request):
    fobj=student_form1()
    return render(request, 'index1.html',{'student':fobj})
