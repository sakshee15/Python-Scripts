import time
import random as rnd
from datetime import datetime
import requests


now=datetime.now()
while True:
    url="http://172.104.207.9:8000/device?uid=5678"
    Date=now.strftime("%d%m")
    Time=now.strftime("%H%M%S")
    Vt1=str( rnd.randint(-100,100))
    Crt= str( rnd.uniform(-10000.00,+10000.00))
    Tp1= str( rnd.uniform(-100.0,+150.0))
    Soc= str( rnd.randint(0,100))
    Uv= rnd.choice(['true','false'])
    Ov= rnd.choice(['true','false'])
    Occ= rnd.choice(['true','false'])
    Ocd= rnd.choice(['true','false'])
    Otc= rnd.choice(['true','false'])
    Otd= rnd.choice(['true','false'])
    URL= url+"&date="+Date+"&time= "+Time+"&vt1="+Vt1+"&crt="+Crt+"&tp1="+Tp1+"&soc="+Soc+"&uv="+Uv+"&ov="+Ov+"&occ="+Occ+"&ocd="+Ocd+"&otc="+Otc+"&otd="+Otd
    r = requests.get(URL,verify=False) 
    data = r.content  # Content of response
    print(r.status_code)  # Status code of response
    print(data)
    time.sleep(10)

    # Ip=172.104.207.9
    # URL=localhost:8000/device?uid=5678&date=1905&time=768&vt1=184&crt=5&tp1=23&soc=12&uv=false&ov=false&occ=false&ocd=false&otc=false&otd=false