from net_system.models import NetworkDevice, Credentials
import django
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from multiprocessing import Process
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
    procs=[]
    for a_device in devices:
        a_process=Process(target=show_version,args=(a_device,))
        a_process.start()
        procs.append(a_process)
    for a_proc in procs:
        a_proc.join()
        
    elapsed_time=datetime.now() - start_time
    print 'Elapsed time is {}'.format(elapsed_time)

if __name__ == "__main__":
    main()


