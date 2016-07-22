from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()

    std_creds=creds[0]
    arista_creds=creds[1]

    for a_device in devices:
       if 'pynet-sw' in a_device.device_name:
           a_device.credentials=arista_creds
       else: 
           a_device.credentials=std_creds
       a_device.save()

    for a_device in devices:
        print a_device.device_name,a_device.credentials


if __name__ == "__main__":
    main()


