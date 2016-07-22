from net_system.models import NetworkDevice, Credentials
import django
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from multiprocessing import Process,Queue
#password=getpass()

def show_arp_queue(a_device,q):
     output_dict={}
     remote_conn=ConnectHandler(device_type=a_device.device_type,ip=a_device.ip_address,username=a_device.credentials.username,password=a_device.credentials.password,port=a_device.port,secret='')
     output= '\n'
     output+= '#' * 80
     output+= remote_conn.send_command("show arp")
     output_dict[a_device.device_name]=output
     q.put(output_dict)


def main():
    django.setup()
    q=Queue(maxsize=20)
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()
    start_time=datetime.now()
    procs=[]
    for a_device in devices:
        a_process=Process(target=show_arp_queue,args=(a_device,q))
        a_process.start()
        procs.append(a_process)
    
    for a_proc in procs:
        a_proc.join()
    
    while not q.empty():
        my_dict=q.get()
        for k,v in my_dict.iteritems():
            print k
            print v

    elapsed_time=datetime.now() - start_time
    print 'Elapsed time is {}'.format(elapsed_time)

if __name__ == "__main__":
    main()


