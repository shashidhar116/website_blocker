import time
from datetime import datetime as dt

hostspath = '/etc/hosts'

redirect = '127.0.0.1'
websitelist = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print('WebSite Not Allowed!!')
        with open(hostspath, 'r+') as file:
            content = file.read()
            for site in websitelist:
                if site in content: pass
                else: file.write(redirect + ' ' + site + '\n')
    else:
        with open(hostspath, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for i in content:
                if not any(site in i for site in websitelist):
                    file.write(i)

            file.truncate()
        print('WebSite is Allowed')

    time.sleep(8)