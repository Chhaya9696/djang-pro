from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm   # for signin view
from django.contrib.auth import authenticate, login, logout
from .models import batch
# from .models import Feedback
from .forms import batchforms
from .forms import Signupform
# from .forms import feedbackform
def index(request):
    return render(request,'index.html')


def createbatch(request):
    if request.method == 'POST':
        cb = batchforms(request.POST)
        if cb.is_valid():
            # batchno','module','time','labno'
            btno=cb.cleaned_data['batchno']
            mdl = cb.cleaned_data['module']
            time = cb.cleaned_data['time']
            lbno = cb.cleaned_data['labno']
            reg1=batch(batch=btno,module=mdl,time=time,labno=lbno)
            reg1.save()
        # Redirect with URL path
        # return redirect('/home/showbatch/')

        # Redirect with URL name
        return redirect('showbatch')
    else:
        cb = batchforms()

    return render(request, 'createbatch.html', {'createbatch': cb})

def showbatch(request):
    batch_data = batch.objects.all()
    return render(request,'batchdetails.html',{'batch':batch_data})
def showdetail(request):
    # select * from batch class
    batch_data = batch.objects.all()
    return render(request,'showdetail.html',{'batch1':batch_data})



def signup(request):
    if request.method == 'POST':
        fm = Signupform(request.POST)
        if fm.is_valid():
            fm.save()
        # Redirect with URL path
        return redirect("signin")
    else:
        fm=Signupform()
    return render(request,'register.html',{'reg_fm':fm})


def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            # feed = FeedbackEntry()
            if user is not None:
                login(request, user)  # username
                return render(request, 'feedback.html', {'user': user})
                # return redirect("/feedback")

    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})

def signout(request):
    logout(request)
    return redirect("/signin")
# def feedback(request):
#     if request.method == 'POST':
#         formfeed=feedbackform(request.POST)
#         if formfeed.is_valid():
#            formfeed.save()
#            return redirect('feedback success')
#     else:
#         formfeed=feedbackform()
#             # redirect('home') //redirect to any page you wish to send the user after registration
#     return render(request, 'feedback.html',{'formf':formfeed})