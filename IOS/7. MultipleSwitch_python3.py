import telnetlib
import getpass

Host = "localhost"
Username = "admin"
Password = "cisco"


with open("config.txt",'r') as config:
    for host in config:
        host = host.strip()
        Host = host
        print("Configuring Switch "+Host)
        tel = telnetlib.Telnet(Host)
        tel.read_until(b"Username: ")
        tel.write(Username.encode("ascii") + b'\n')

        if Password:
            tel.read_until(b"Password: ")
            tel.write(Password.encode('ascii') + b"\n")
        tel.write(b"conf t \n")

        for N in range (2,10):
            N = str(N)
            tel.write(b"vlan "+ N.encode('ascii')+ b'\n')
            tel.write(b"name python_vlan_" + N.encode('ascii') + b'\n')

        tel.write(b'end\n')
        tel.write(b'exit\n')

        print(tel.read_all().decode('ascii'))
