from django.urls import path
from app1 import views
urlpatterns = [
    path('createbatch/', views.createbatch,name='createbatch'),
    path('index/', views.index),
    path('showbatch/', views.showbatch,name='showbatch'),
    path('showdetail/', views.showdetail,name='showdetail'),
    # path('batchdetails/', views.batchdetails,name='batchdetails'),
    path('signup/', views.signup,name='register'),
    path('signin/', views.signin,name="signin"),
    path('logout/', views.signout),
    # path('feedback/', views.feedback),

]
