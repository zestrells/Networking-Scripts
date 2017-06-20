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
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH Connection is being established to %s" % ip
    #Invoke_shell is establishing an interactive session
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session has been established."
    #Outputs the initial router console
    output = remote_conn.recv(1000)
    print output
    #Turn off limiting of paging
    disable_paging(remote_conn)

def enable_gigabyte00(remote_conn):
    #Activates gigabyte 0/0
    remote_conn.send("\n")
    remote_conn.send("")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("int gigabitethernet0/0")
    time.sleep(2)
    remote_conn.send("ip address 192.168.1.1 255.255.255.255")
    time.sleep(2)
    remote_conn.send("no shutdown")

def enable_gigabyte01(remote_conn):
    #Activates gigabyte 0/1
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("int gigabitethernet0/1")
    time.sleep(2)
    remote_conn.send("ip address 192.168.1.1 255.255.255.255")
    time.sleep(2)
    remote_conn.send("clock rate 64000")
    time.sleep(2)
    remote_conn.send("no shutdown")

def enable_gigabyte02(remote_conn):
    #Activates gigabyte 0/2
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("int gigabitethernet0/2")
    time.sleep(2)
    remote_conn.send("ip address 192.168.1.1 255.255.255.255")
    time.sleep(2)
    remote_conn.send("clock rate 64000")
    time.sleep(2)
    remote_conn.send("no shutdown")


def enable_ospf(remote_conn):
    #Activates OSPF on the switch
    remote_conn.send("\n")
    remote_conn.send("enable")
    time.sleep(2)
    remote_conn.send("configuration terminal")
    time.sleep(2)
    remote_conn.send("router ospf 1")
    time.sleep(2)
    #remote_conn.send("router-id 1.1.1.1")
    #time.sleep(2)
    remote_conn.send("network 10.1.1.1 0.0.0.0 area 1")
    time.sleep(2)
    remote_conn.send("network 10.1.2.1 0.0.0.0 area 1")
    time.sleep(2)
    remote_conn.send("network 192.168.10.1 0.0.0.0 area 0")
    time.sleep(2)
    remote_conn.send("end")

# Switch being connected to
    ip = '192.168.1.1'
    user = 'testuser'
    password = 'cisco'