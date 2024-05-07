#!/usr/bin/python3
import requests
import logging
import time
from urllib.request import urlopen

ddns_dict = {
    'sub-domain':{
        'username':'usr',
        'password':'pwd',
        'hostname':'sub-domain.domain.com'
    },
    'sub-domain2':{
        'username':'usr2',
        'password':'pwd2',
        'hostname':'sub-domain2.domain.com'
    },
    ...
}

logging.basicConfig(filename='ddns.log', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(message)s')
old_ip = ''

while True:
    username = ''
    password = ''
    hostname = ''
    try:
        my_ip = urlopen('https://domains.google.com/checkip').read() 
    except:
        logging.debug('CATCHED AN ERROR... RETRYING IN 10 SECONDS')
        time.sleep(10)
    else:
        if my_ip != old_ip:
            for key, value in ddns_dict.items():
                username = value['username']
                password = value['password']
                hostname = value['hostname']
                url = 'https://{}:{}@domains.google.com/nic/update?hostname={}'.format(username, password, hostname)
                response = requests.post(url)
                output = response.content.decode('utf-8')
                if 'good' in output or 'nochg' in output:
                    old_ip = my_ip
                logging.debug('-- OUTPUT FOR UPDATE: '+ hostname +' --')
                logging.debug('Response from DDNS update: '+ output)
        time.sleep(10)