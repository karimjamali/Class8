#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass


def main():

    password=getpass()

    pynet1={
        'device_type':'cisco_ios',
        'ip':'184.105.247.70',
        'username':'pyclass',
        'password':password,
        'port': 22
    }

    pynet2={
        'device_type':'cisco_ios',
        'ip':'184.105.247.71',
        'username':'pyclass',
        'password':password,
        'port': 22,
}


    juniper_srx = {
        'device_type':'juniper',
        'ip':'184.105.247.76',
        'username':'pyclass',
        'password': password,
        'secret':'',
        'port': 22, 
    }

    #print pynet1[1]
    for a_device in (pynet1,pynet2):
        Connection=ConnectHandler(**a_device)
        Connection.send_config_from_file(config_file='my_config.txt')
        result=Connection.send_command('show run | inc logging')
        print '\n\n'
        print '#' * 80
        print a_device['ip'], '\n',result
        print '#' * 80
        print '\n\n'


if __name__ =="__main__":
    main()
