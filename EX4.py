from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()
    
    #test_rtr1 = NetworkDevice.objects.get(device_name='test-rtr1')
    #test_rtr2 = NetworkDevice.objects.get(device_name='test-rtr2')
    #print test_rtr1
    #print test_rtr2

    try:
        test_rtr1 = NetworkDevice.objects.get(device_name='test-rtr1')
        test_rtr2 = NetworkDevice.objects.get(device_name='test-rtr2')
        #print test_rtr1
        #print test_rtr2
        test_rtr1.delete()
        test_rtr2.delete()
    except NetworkDevice.DoesNotExist:
        pass


    for a_device in devices:
        print a_device


if __name__ =="__main__":
    main()
