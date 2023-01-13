from netmiko import ConnectHandler
from datetime import datetime
import time

start_time = datetime.now()
all_routers = ["10.255.1.101", "10.255.1.102", "10.255.1.103", "10.255.1.104", "10.255.1.105"]
myfile = open("/home/student/Desktop/DEVNET TEST/output_without_mt.txt", "a")

for router in all_routers:
    ssh = ConnectHandler(
        device_type="cisco_ios",
        host=router,
        username="admin",
        password="cisco"
    )

    int_brief = ssh.send_command("show ip int brief")
    myfile.write(int_brief)
    

print("Time taken to run the script: " + str((datetime.now() - start_time)))
