import os
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
from datetime import date


USEERNAME = input('Enter your SSH user : ')
PASSWORD = getpass('Enter your SSH Pass : ')
DATE = date.today().strftime("%y_%m_%d")

device={
    'ip' :'192.168.176.10',
    'username' : USEERNAME ,
    'password' : PASSWORD,
    'device_type' : 'cisco_ios'    
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open(f'backup_config{DATE}','x')

f.write(output)
f.close