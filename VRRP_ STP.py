#import netmiko import ConnectHandler
from datetime import datetime

class Router():



    def __init__(self):

        self.ip = ip
        start_time = datetime.now()
        self.credentials()


        self.credentials
    def credentials(self):
        self.router1 = {
            'device_type': 'cisco_ios',
            'ip': '10.10.10.10',
            'username': 'test',
            'password': 'cisco'
        }
        self.router2 = {
            'device_type': 'cisco_ios',
            'ip': '20.20.20.20',
            'username': 'test',
            'password': 'cisco'
        }

        self.router3 = {
            'device_type': 'cisco_ios',
            'ip': '30.30.30.30',
            'username': 'test',
            'password': 'cisco'
        }

        self.all_devices = [
            router1,
            router2,
            router3
        ]
    def configurationAdjustments(self):
        self.config_commands = ['enable',
                                'configuration terminal',
                                'int gigabitethernet0/0',
                                'ip address 0.0.0.0',  # changes the ip address of 0/0
                                'no shutdown',
                                'int gigabitethernet0 / 1',
                                'ip address 0.0.0.0',  # changes the ip address of 0/1
                                'no shutdown'
                                'int gigabitethernet0/2',
                                'ip address 0.0.0.0',  # changes the ip address of 0/2
                                'no shutdown'
                                'interface gigabitethernet0/1',  # Change this according to which port is VRRP
                                'vrrp 1 0.0.0.0',  # change the VRRP number here
                                'vrrp 1 description automated',  # change the priority level for VRRP here
                                'vrrp 1 100']  # change priority
        self.maxConfig = self.maxRouter
        for c in enumerate(self.config_commands):
            pass

        output = net_connect.send_config_set(config_commands)
        print(output)

    def userInput():
        self.num_of_Routers = int(raw_input('How many routers are you configuring? '))
        self.router = {}
        for router in range(self.num_of_Routers):
            self.num_Router = raw_input('Which router are you configuring?')
            print 'Enter the IP address followed by the subnet mask.\n Ex: 192.168.1.1 255.255.255.255'
            self.int_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
            self.int_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
            self.int_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
            print 'Enter the VRRP IP Address followed by the priority number. \n'
            self.vrrp_ip = raw_input('Enter the VRRP IP Address: ')
            self.vrrp_priority = raw_input('Enter the VRRP priority number: ')
            self.vrrp_interface = raw_input('Enter the VRRP Interface: ')
        print('All routers have been configured, moving on!')

userInput()
#def connection(auth):
#    start_time = datetime.now()
#    for a_device in auth.all_devices:
#        if auth.router1(auth):
#            net_connect = ConnectHandler(auth.router1)
#            net_connect.enable()
#            print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
#
#        output = net_connect.send_config_set(config_commands)
#main()












