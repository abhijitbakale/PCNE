from netmiko import ConnectHandler
import time
from datetime import datetime
import concurrent.futures

start_time = datetime.now()

R1 = {
        'device_type':'cisco_ios',
        'host':'10.255.1.101',
        'username':'admin',
        'password':'cisco'
    }

R2 ={
        'device_type':'cisco_ios',
        'host':'10.255.1.102',
        'username':'admin',
        'password':'cisco'
    }

R3 = {
        'device_type':'cisco_ios',
        'host':'10.255.1.103',
        'username':'admin',
        'password':'cisco'
    }

R4 = {
        'device_type':'cisco_ios',
        'host':'10.255.1.104',
        'username':'admin',
        'password':'cisco'
    }

R5 = {
        'device_type':'cisco_ios',
        'host':'10.255.1.105',
        'username':'admin',
        'password':'cisco'
    }

myfile = open("/home/student/Desktop/DEVNET TEST/output_with_mt.txt", "a")
def device_connect(device_dict):
    ssh = ConnectHandler(**device_dict)
    print("SSH Connection EST with " + device_dict["router"])
    int_brief = ssh.send_command("show ip int brief")
    myfile.write(int_brief)

all_routers = [R1, R2, R3, R4, R5]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(device_connect, all_routers)

print("Time taken to run the script: " + str((datetime.now() - start_time)))