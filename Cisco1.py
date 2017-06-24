import paramiko
import time


def disable_paging(remote_conn):
    '"Disable paging on a Cisco router"'
    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    # Clear the buffer on the screen
    output = remote_conn.recv(1000)
    return output

def init_conn(remote_conn):
    #Creates the SSHClient connection
    remote_conn_pre = paramiko.SSHClient()
    #Adds untrusted hosts
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #initiate SSH connection
    try:
        remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    except paramiko.AuthenticationException:
        print "[-] Authentication Exception! ..."
    except paramiko.SSHException:
        print "[-] SSH Exception! ..."

    print "SSH Connection is being established to %s" % ip
    #Invoke_shell is establishing an interactive session
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session has been established."
    #Outputs the initial router console
    output = remote_conn.recv(1000)
    print output
    #Turn off limiting of paging
    disable_paging(remote_conn)

def gigabyte00(remote_conn):
    #Activates gigabyte 0/0 on R1
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("int gigabitethernet0/0")
    time.sleep(2)
    remote_conn.send("ip address %s" % (00)) #change this depending on IP config
    time.sleep(2)
    remote_conn.send("no shutdown")

def gigabyte01(remote_conn):
    #Activates gigabyte 0/1
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("int gigabitethernet0/1")
    time.sleep(2)
    remote_conn.send("ip address %s" % (01)) #change this depending on IP config
    time.sleep(2)
    remote_conn.send("no shutdown")

def gigabyte02(remote_conn):
    #Activates gigabyte 0/2 on r1
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("int gigabitethernet0/2")
    time.sleep(2)
    remote_conn.send("ip address %s" % (02)) #change this depending on IP config
    time.sleep(2)
    remote_conn.send("no shutdown")


def vrrp(remote_conn):
    #Activates VRRP on r1
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("interface gigabitethernet") #Change this according to which port is VRRP
    time.sleep(2)
    remote_conn.send("vrrp 1 ip 10.10.10.5") #change the VRRP number here
    time.sleep(2)
    remote_conn.send("vrrp 1 description SDN") #change the priority level for VRRP here
    time.sleep(2)
    remote_conn.send("vrrp 1 priority 110")
    time.sleep(2)
    remote_conn.send("end")




# Router being connected to
    ip = '192.168.1.1'
    user = 'testuser'
    password = 'cisco'

def main():
    print 'Configuring STP and VRRP \n Router 1'
    print 'Enter the IP address followed by the subnet mask \n Ex: 192.168.1.1 255.255.255.255'
    r1_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
    r1_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
    r1_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
    print 'Switch 2'
    r2_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
    r2_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
    r2_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')
    print 'Switch 3'
    r3_00 = raw_input('Enter GigabitEthernet0/0 IP Address: ')
    r3_01 = raw_input('Enter GigabitEthernet0/1 IP Address: ')
    r3_02 = raw_input('Enter GigabitEthernet0/2 IP Address: ')

    #init_conn(remote_conn);
    #r1_gigabyte00(remote_conn);
    #r1_gigabyte01(remote_conn);
    #r1_gigabyte02(remote_conn);

main()