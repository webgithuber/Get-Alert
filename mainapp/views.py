from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render , redirect
import http.client
import json
import datetime
from mainapp.models import Centers
import math, random
from django.core.mail import send_mail
# Create your views here.
v={} # likly center
z={} #for center list(choosen) for object
all_cntr=''
def home(request):
    try:
        value = request.COOKIES['active']
        return render(request,'front.html',{'status':int(value)})
    except:
        zero=0
        response= render(request,'front.html',{'status':zero})
        response.set_cookie('active','0')
        return response
    
def getdata(request):
    context_object_name='c'
    st_id=request.GET['select_state']
    dst_id=request.GET['select_district']
    # pin=request.GET['pin']
    pin=''
    if pin=="":
        date=request.GET['date']  
        date1 = datetime.date(2021, 7, 10)
        date2 = datetime.date(2021, 7, 19)
        day = datetime.timedelta(days=1)   
        conn = http.client.HTTPSConnection("cdn-api.co-vin.in")

        headers = {
            'cache-control': "no-cache",
            'postman-token': "d621c9d0-fbef-046b-6899-a9aa41dd4463"
            }

        conn.request("GET", "/api/v2/admin/location/states", headers=headers)

        res = conn.getresponse()
        data = res.read()
        my_json = data.decode('utf8').replace("'", '"')
        data_dst = json.loads(my_json)
        # print(data_dst)
        


        headers = {
            'cache-control': "no-cache",
            'postman-token': "d58dcf94-e430-e7d2-34b5-33053fa2c3d8"
            }


        dis = {
            'cache-control': "no-cache",
            'postman-token': "9266b2b3-cdb4-1ce4-e21a-7df331c723c8"
            }
        centers={}
        date1 = datetime.date(2021, 6, 25)
        date2 = datetime.date(2021, 7, 23)
        day = datetime.timedelta(days=1)
        while date1 <= date2:
            s=str(date1.day) + '-' + str(date1.month) + '-' + str(date1.year)
            conn.request("GET", "/api/v2/appointment/sessions/public/findByDistrict?district_id="+dst_id+"&date="+s, headers=dis)
            date1 = date1 + day
            res = conn.getresponse()
            d_c = res.read()
            my = d_c.decode('utf8').replace("'", '"')
            d_c = json.loads(my)
            for c in d_c['sessions']:
                centers[c['name']]=c['center_id']
                
            try:   
                all_cntr=Centers.objects.all().filter(Email=request.COOKIES['mail'])
                for cntr in all_cntr:
                    centers.pop(cntr.Center_name)
            except:
                pass
        temp=[]
        a=[]
        for key, value in centers.items():
            temp = [key,value]
            a.append(temp)
        
        v['q']=a
        try:
           v['status'] = int(request.COOKIES['active'])
           return render(request,'front.html',v)
        except:
            v['status']=0
            return render(request,'front.html',v)
    else:
        pass
def add(request,x,y):

    try:
        data2 = Centers.objects.get(Email=request.COOKIES['mail'],Center_name=x,Center_id=y)
    except Centers.DoesNotExist:
        data2 = None
    if  data2==None :
        data=Centers.objects.create(Email=request.COOKIES['mail'],Center_name=x,Center_id=y)
        data.save()
        v['q'].remove([x,int(y)])
    return render(request,'front.html',v)

def gotolist(request):
    try:
        all_cntr=Centers.objects.all().filter(Email=request.COOKIES['mail'])
    except Centers.DoesNotExist:
        all_cntr = None
    
    z['a']=all_cntr #object-list
    z['status']=int(request.COOKIES['active'])
    return render(request,'center_list.html',z)

def dlt(request,name):
    Centers.objects.filter(Email=request.COOKIES['mail'],Center_name=name).delete()
    return gotolist(request)

def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')

def sendOtp(request):
    mail_id=request.GET['mail_id']
    msg="Your OTP for GetAlert varification is "
    otp=""
    digits="0123456789"
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    msg+=otp
    msg+=" and OTP will expire after 3 minute"
    send_mail('GetAlert varification OTP ',msg,'englishhindunews2020@gmail.com', [mail_id], fail_silently=False,)
    response=render(request,'verify_otp.html')
    response.set_cookie('otp',otp ,max_age=180)
    response.set_cookie('mail',mail_id)
    return response


def verifyOtp(request):
    O_T_P=request.GET['otp']
    if O_T_P  == request.COOKIES['otp']:
        respns=render(request,'front.html',{'status':1})
        respns.set_cookie('active','1')
        return respns
    else:
        return render(request,'verify_otp.html') 


def logout(request):
    response= redirect('/home/')
    response.delete_cookie('active')
    response.delete_cookie('mail')
    return response

	


