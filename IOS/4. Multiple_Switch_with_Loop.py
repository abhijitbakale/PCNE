import getpass
import telnetlib
import sys

HOST = "localhost"
username = raw_input("Enter Your Username: ")
password = getpass.getpass()


a = open('myswitches')  # myswitches_is_a_.txt_containing_ip_addresses

for IP in a:

    print IP
    IP = IP.strip()
    HOST = IP
    print ("Configuring Switch " + HOST)
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(username + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("enable\n")
    tn.write("cisco\n")  # enable password is cisco
    tn.write("configure terminal\n")

    for n in range(2,10):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_VLAN_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
