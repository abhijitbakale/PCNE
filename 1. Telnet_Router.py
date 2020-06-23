import getpass
import telnetlib

HOST = "192.168.240.160"
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
tn.write("interface loopback 10\n")
tn.write("ip address 10.10.100.1 255.255.255.0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
