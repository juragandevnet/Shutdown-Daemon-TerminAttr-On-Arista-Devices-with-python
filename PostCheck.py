### IT IS CREATED BY JURAGAN DEVNET   ###
### https://youtube.com/@juragandevnet ###
### https://github.com/juragandevnet  ###

from netmiko import ConnectHandler 
from threading import Thread

def upload(device_type, username, password, ip_address):
    iosv2_l2 = {
        'device_type' : device_type,
        'ip' : ip_address,
        'username': username,
        'password': password 
    }
    net_connect = ConnectHandler(**iosv2_l2)
    output_hostname = net_connect.send_command('show run | i hostname')
    output_ios = net_connect.send_command("show daemon TerminAttr")
    print(output_hostname)
    print(output_ios)
    net_connect.disconnect()

f = open('devices.txt','r')  
print("Pre Check Report: ")
threads=[]
threads = [Thread(target=upload, args=('arista_eos','catadmin_2','yj%Ve6Yu~y', ip_address)) for ip_address in f.readlines()]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
