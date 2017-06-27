import netmiko import ConnectHandler
from datetime import datetime

class Router():
    def __init__(self):
        start_time = datetime.now()
        for self.a_device in credentials(self.all_devices):
            net_connect = ConnectHandler(**self.a_device)



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
    def r1(self):
        config_commands = ['enable',
                           'configuration terminal',
                           'int gigabitethernet0/0',
                           'ip address %s' % router.r1_00,  # changes the ip address of 0/0
                           'no shutdown',
                           'int gigabitethernet0 / 1',
                           'ip address %s' % router.r1_01,  # changes the ip address of 0/1
                           'no shutdown'
                           'int gigabitethernet0/2',
                           'ip address %s' % router.r1_02,  # changes the ip address of 0/2
                           'no shutdown'
                           'interface gigabitethernet',  # Change this according to which port is VRRP
                           'vrrp 1 ip %s' % router.vrrp_ip1,  # change the VRRP number here
                           'vrrp 1 description automated',  # change the priority level for VRRP here
                           'vrrp 1 %s' % router.vrrp_priority1]  # change priority
        output = net_connect.send_config_set(config_commands)
        print(output)
    def r2(self):
        config_commands = ['enable',
                           'configuration terminal',
                           'int gigabitethernet0/0',
                           'ip address %s' % router.r2_00,  # changes the ip address of 0/0
                           'no shutdown',
                           'int gigabitethernet0/1',
                           'ip address %s' % router.r2_01,  # changes the ip address of 0/1
                           'no shutdown'
                           'int gigabitethernet0/2',
                           'ip address %s' % router.r1_02,  # changes the ip address of 0/2
                           'no shutdown'
                           'interface gigabitethernet',  # Change this according to which port is VRRP
                           'vrrp 1 ip %s' % router.vrrp_ip2,  # change the VRRP number here
                           'vrrp 1 description automated',  # change the priority level for VRRP here
                           'vrrp 1 %s' % router.vrrp_priority2]  # change priority
        output = net_connect.send_config_set(config_commands)
        print(output)
    def r3(self):
        config_commands = ['enable',
                           'configuration terminal',
                           'int gigabitethernet0/0',
                           'ip address %s' % router.r3_00,  # changes the ip address of 0/0
                           'no shutdown',
                           'int gigabitethernet0 / 1',
                           'ip address %s' % router.r3_01,  # changes the ip address of 0/1
                           'no shutdown'
                           'int gigabitethernet0/2',
                           'ip address %s' % router.r3_02,  # changes the ip address of 0/2
                           'no shutdown'
                           'interface gigabitethernet',  # Change this according to which port is VRRP
                           'vrrp 1 ip %s' % router.vrrp_ip3,  # change the VRRP number here
                           'vrrp 1 description automated',  # change the priority level for VRRP here
                           'vrrp 1 %s' % router.vrrp_priority3]  # change priority
        output = net_connect.send_config_set(config_commands)
        print(output)

def main(router):
    print 'Configuring STP and VRRP \n Router 1'
    print 'Enter the IP address followed by the subnet mask and VRRP \n Ex: 192.168.1.1 255.255.255.255'
    router.r1_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
    router.r1_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
    router.r1_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
    router.vrrp_ip1 = raw_input('Enter the VRRP IP Address: ')
    router.vrrp_priority1 = raw_input('Enter the VRRP priority number: ')
    print 'Router 2'
    router.r2_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
    router.r2_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
    router.r2_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
    router.vrrp_ip2 = raw_input('Enter the VRRP IP Address: ')
    router.vrrp_priority2 = raw_input('Enter the VRRP priority number: ')
    print 'Router 3'
    router.r3_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
    router.r3_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
    router.r3_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
    router.vrrp_ip3 = raw_input('Enter the VRRP IP Address: ')
    router.vrrp_priority3 = raw_input('Enter the VRRP priority number: ')


def connection(auth):
    start_time = datetime.now()
    for a_device in auth.all_devices:
        if auth.router1(auth):
            net_connect = ConnectHandler(auth.router1)
            net_connect.enable()
            print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())

        outut = net_connect.send_config_set(config_commands)
main()












