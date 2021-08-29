
from mainapp import views
from django.urls import path

app_name = "mainapp"
urlpatterns = [
    
    path("",views.home,name="home"),
    path("send",views.getdata,name="getdata"),
    path("add/(?P<x>)/(?P<y>)/$",views.add,name="add"),
    path("cntr-list",views.gotolist,name="gtlist"),
    path("dlt/(?P<name>)/$",views.dlt,name="dltcntr"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("sendOtp",views.sendOtp,name="sendOtp"),
    path("verifyOtp",views.verifyOtp,name="verifyOtp"),
    path('logout',views.logout,name="logout") 
   
]