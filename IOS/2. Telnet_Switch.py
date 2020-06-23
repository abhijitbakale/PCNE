import getpass
import telnetlib

HOST = "192.168.240.101"
username = raw_input("Enter Your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(username + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")  # enable password is cisco
tn.write("configure terminal\n")
tn.write("vlan 10\n")
tn.write("name Python_VLAN_10\n")
tn.write("vlan 20\n")
tn.write("name Python_VLAN_20\n")
tn.write("vlan 30\n")
tn.write("name Python_VLAN_30\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
