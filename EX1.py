from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()
    devices=NetworkDevice.objects.all()
    creds=Credentials.objects.all()
    print '\n\n'
    print devices 
    print '\n\n'
    print creds

if __name__ =="__main__":
    main()
