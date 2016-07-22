from net_system.models import NetworkDevice, Credentials
import django
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import threading
#password=getpass()

def show_version(a_device):
     remote_conn=ConnectHandler(device_type=a_device.device_type,ip=a_device.ip_address,username=a_device.credentials.username,password=a_device.credentials.password,port=a_device.port,secret='')
     print '\n'
     print '#' * 80
     print remote_conn.send_command("show version")
     print '#' * 80
     print '\n'


def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()
    start_time=datetime.now()
    for a_device in devices:
        a_thread=threading.Thread(target=show_version,args=(a_device,))
        a_thread.start()

    main_thread=threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()
        
    elapsed_time=datetime.now() - start_time
    print 'Elapsed time is {}'.format(elapsed_time)

if __name__ == "__main__":
    main()

