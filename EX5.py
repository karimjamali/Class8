from net_system.models import NetworkDevice, Credentials
import django
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

#password=getpass()

def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()
    start_time=datetime.now()
    for a_device in devices:
        #print a_device
        device_type=a_device.device_type
        port=a_device.port
        ip=a_device.ip_address
        #creds=a_device.credentials
        username=a_device.credentials.username
        password=a_device.credentials.password
        #print device_type,ip,port,username,password
        remote_conn=ConnectHandler(device_type=device_type,ip=ip,                               username=username,password=password,port=port)
        print '\n'
        print '#' * 80
        print remote_conn.send_command("show version")
        print '#' * 80
        print '\n'
    elapsed_time=datetime.now() - start_time
    print 'Elapsed time is {}'.format(elapsed_time)

if __name__ == "__main__":
    main()
