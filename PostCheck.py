### IT IS CREATED BY JURAGAN DEVNET   ###
### https://youtube.com/@juragandevnet ###
### https://github.com/juragandevnet  ###

import getpass
import re
from netmiko import ConnectHandler 
from threading import Thread

def upload(device_type, username, password, ip_address):
    SshLogin = {
        'device_type' : device_type,
        'ip' : ip_address,
        'username': username,
        'password': password 
    }
    net_connect = ConnectHandler(**SshLogin)
    host = net_connect.send_command('show run | i hostname')
    output_hostname = re.search(r"\b(\w+)$", host) 
    output_eos = net_connect.send_command("show daemon TerminAttr")
    print(output_hostname)
    print(output_eos)
    net_connect.disconnect()

### READ devices.txt file ###
f = open('devices.txt','r')  

### INPUT FOR USERNAME AND PASSWORD ###
username = ("Username: ")
password = getpass.getpass()

print("Pre Check Report: ")

### THREAD PROCESS ###
threads=[]
threads = [Thread(target=upload, args=('arista_eos', username, password, ip_address)) for ip_address in f.readlines()]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
