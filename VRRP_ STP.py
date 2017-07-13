#import netmiko import ConnectHandler
from datetime import datetime

class UserInput():

    def __init__(self):
        self.routers = {}
        self.num_of_Routers = 0
        while True:
            try:
                self.num_of_Routers = int(raw_input('How many routers are you configuring? '))
            except ValueError:
                print("Please enter a correct number of Routers!")
                continue
            else:
                break

    def quantity(self):
        for num in range(self.num_of_Routers):
            self.routers['router ' + str(num)] = {}
        print(self.routers)

    def configuration(self):
        for router in range(self.num_of_Routers):
            print 'Enter the configuration for Router ' + str(router)
            print 'Enter the IP address followed by the subnet mask.\n Ex: 192.168.1.1 255.255.255.255'
            self.routers['router ' + str(router)] = int_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
            int_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
            int_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
            print 'Enter the VRRP IP Address followed by the priority number. \n'
            vrrp_ip = raw_input('Enter the VRRP IP Address: ')
            vrrp_priority = raw_input('Enter the VRRP priority number: ')
            vrrp_interface = raw_input('Enter the VRRP Interface: ')
            self.router_config['router' + str(router)] = [int_00, int_01, int_02, vrrp_ip, vrrp_priority, vrrp_interface]
            print (router_config)
        print('All routers have been configured, moving on!')

class Router():
    routers_configured = False


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
        self.router_commands1 = ['enable',
                                'configuration terminal',
                                'int gigabitethernet0/0',
                                'ip address ',  # changes the ip address of 0/0
                                'no shutdown',
                                'int gigabitethernet0/1',
                                'ip address ',  # changes the ip address of 0/1
                                'int gigabitethernet0/2',
                                'ip address ',  # changes the ip address of 0/2
                                'interface gigabitethernet0/1',  # Change this according to which port is VRRP
                                'vrrp 1 ',  # change the VRRP number here
                                'vrrp 1 description automated',  # change the priority level for VRRP here
                                'vrrp 1 ', #changebrrp priority
                                'do show vrrp brief']

        self.router_commands2 = ['enable',
                                'configuration terminal',
                                'int gigabitethernet0/0',
                                'ip address ',  # changes the ip address of 0/0
                                'no shutdown',
                                'int gigabitethernet0/1',
                                'ip address ',  # changes the ip address of 0/1
                                'int gigabitethernet0/2',
                                'ip address ',  # changes the ip address of 0/2
                                'interface gigabitethernet0/1',  # Change this according to which port is VRRP
                                'vrrp 1 ',  # change the VRRP number here
                                'vrrp 1 description automated',  # change the priority level for VRRP here
                                'vrrp 1 ', #changebrrp priority
                                'do show vrrp brief']
        self.router_commands3 = ['enable',
                                'configuration terminal',
                                'int gigabitethernet0/0',
                                'ip address ',  # changes the ip address of 0/0
                                'no shutdown',
                                'int gigabitethernet0/1',
                                'ip address ',  # changes the ip address of 0/1
                                'int gigabitethernet0/2',
                                'ip address ',  # changes the ip address of 0/2
                                'interface gigabitethernet0/1',  # Change this according to which port is VRRP
                                'vrrp 1 ',  # change the VRRP number here
                                'vrrp 1 description automated',  # change the priority level for VRRP here
                                'vrrp 1 ', #changebrrp priority
                                'do show vrrp brief']
        for router in range(self.num_of_Routers):
            self.router_commands1.insert[3] = 'ip address' + userInput.router1.int_00
        output = net_connect.send_config_set(config_commands)
        print(output)
    def establishConnection(self):
        for router in range(self.num_of_Routers):
            output = net_connect.send_config_set(self.router_commands.values())
ui = UserInput()
ui.quantity()
ui.configuration()


#def connection(auth):
#    start_time = datetime.now()
#    for a_device in auth.all_devices:
#        if auth.router1(auth):
#            net_connect = ConnectHandler(auth.router1)
#            net_connect.enable()
#            print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
#
#        output =