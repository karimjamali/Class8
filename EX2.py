from net_system.models import NetworkDevice, Credentials
import django


def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()

    std_creds=creds[0]
    arista_creds=creds[1]

    for a_device in devices:
        print a_device.device_name, a_device.vendor
        


    for a_device in devices:
       if 'pynet-sw' in a_device.device_name:
           a_device.vendor='Arista'
       elif 'pynet-rtr' in a_device.device_name:
           a_device.vendor='Cisco'
       else:
           a_device.vendor='Juniper'
       a_device.save()

    for a_device in devices:
        print a_device.device_name, a_device.vendor

if __name__ =="__main__":
    main()

