from net_system.models import NetworkDevice, Credentials
import django


def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()

    std_creds=creds[0]
    arista_creds=creds[1]


    test_rtr1 = NetworkDevice(
        device_name='test-rtr1',
        device_type='cisco_ios',
        ip_address='10.1.1.1',
        port=5022,
    )
    test_rtr1.save()

    test_rtr2 = NetworkDevice.objects.get_or_create(
        device_name='test-rtr2',
        device_type='cisco_ios',
        ip_address='10.1.1.2',
        port=5122,
    )
    
    for a_device in devices:
        print a_device.device_name
    




if __name__ =="__main__":
    main()

