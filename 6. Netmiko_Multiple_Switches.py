from netmiko import ConnectHandler

CSW1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.101',
    'username': 'admin',
    'password': 'cisco'
}

DSW1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.102',
    'username': 'admin',
    'password': 'cisco'
}

DSW2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.103',
    'username': 'admin',
    'password': 'cisco'
}

all_devices = [CSW1, DSW1, DSW2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    for n in range(2, 10):
        print ("Configuring Switch" + devices)
        print ("Configuring Vlan " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
