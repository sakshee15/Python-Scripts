import time
import random as rnd
from datetime import datetime
import requests


while True:
    now=datetime.now()
    url="http://172.104.207.9:8000/device?uid=1234"
    Date=now.strftime("%d%m")
    Time=now.strftime("%H%M%S")
    Vt1=str( rnd.randint(0,60))
    Vt2=str( rnd.randint(0,60))
    Crt= str( rnd.uniform(-10000.00,+10000.00))
    Tp1= str( rnd.uniform(-100.0,+150.0))
    Tp2= str( rnd.uniform(-100.0,+150.0))
    Cap=str( rnd.uniform(0.01,100.00))
    Trm=str( rnd.randint(0,10000))
    Soc= str( rnd.randint(0,100))
    Tq1=str( rnd.randint(-50,100))
    Tq2=str( rnd.randint(-50,100))
    Uv= rnd.choice(['true','false'])
    Ov= rnd.choice(['true','false'])
    Occ= rnd.choice(['true','false'])
    Ocd= rnd.choice(['true','false'])
    Otc= rnd.choice(['true','false'])
    Otd= rnd.choice(['true','false'])
    URL= url+"&date="+Date+"&time= "+Time+"&vt1="+Vt1+"&vt2="+Vt2+"&crt="+Crt+"&tp1="+Tp1+"&tp2="+Tp2+"&cap="+Cap+"&trm="+Trm+"&soc="+Soc+"&tq1="+Tq1+"&tq2="+Tq2+"&uv="+Uv+"&ov="+Ov+"&occ="+Occ+"&ocd="+Ocd+"&otc="+Otc+"&otd="+Otd
    r = requests.get(URL,verify=False) 
    data = r.content  # Content of response
    print(r.status_code)  # Status code of response
    print(data)
    time.sleep(10)

    # Ip=172.104.207.9
# URL=localhost:8000/device?uid=1234date=1905&time=768&vt1=184&vt2=567&crt=5&tp1=23&tp2=12&cap=13&trm=9&soc=12&tq1=1&tq2=1&uv=false&ov=false&occ=false&ocd=false&otc=false&otd=false