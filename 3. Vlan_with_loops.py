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

print "ok"
for n in range(2, 12):
    tn.write("vlan " + str(n) + "\n")
    tn.write("name Python_VLAN_" + str(n) + "\n")
    print"VLAN " + str(n) + "created"
tn.write("end")
print"end"
tn.write("exit")
print"exit"
print tn.read_all()

print "ok"
