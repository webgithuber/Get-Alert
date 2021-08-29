from datetime import datetime, date, time, timedelta
from mainapp.models import Centers
from django.core.mail import send_mail
import http.client
import json
conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
headers = {
    'cache-control': "no-cache",
    'postman-token': "4c8cd4ad-906f-720d-2713-dafb8ef3926e"
    }
def Vaccine_availability():
    # print("this function runs every 2 seconds "+ str(datetime.now()))
    mail_id_list=Centers.objects.values('Email').distinct()
    for z in mail_id_list:
        msg="Vaccine available @ this centers "
        count=0
        # print(z['Email'])
        try:
            all_cntr=Centers.objects.all().filter(Email=z['Email'])
        except Centers.DoesNotExist:
            all_cntr = None
        t_o_d_a_y=datetime.today().strftime('%d-%m-%Y')
        for objt in all_cntr:
            conn.request("GET", "/api/v2/appointment/sessions/public/calendarByCenter?center_id="+ objt.Center_id+"&date="+t_o_d_a_y, headers=headers)
            res = conn.getresponse()
            d_c = res.read()
            my = d_c.decode('utf8').replace("'", '"')
            d_c = json.loads(my)
            if d_c['sessions'][0]['available_capacity']>0:
                count=count+1
                msg+=" , "+objt.Center_name
            msg+=" Hurry up and get vaccinated"
            if count>0:
                send_mail('GetAlert Vaccine Availability ',msg,'englishhindunews2020@gmail.com', [z['Email']], fail_silently=False,)






# conn.request("GET", "/api/v2/appointment/sessions/public/calendarByCenter?center_id=1234&date=31-03-2021", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))
def abc():
    Vaccine_availability()