from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.240.162',
    'username': 'admin',
    'password': 'cisco'
}


net_connect = ConnectHandler(**R1)
net_connect.enable()
output = net_connect.send_command('show ip interface brief')
print (output)

config_commands = ('interface loopback 10', 'ip address 101.101.101.1 255.255.255.0')
output = net_connect.send_config_set(config_commands)
print (output)


# How to enable the diffie-hellman-group1-sha1 key exchange method on Debian 8.0?

# I have tried (as proposed here) to
# install open ssh - apt-get install openssh-server

# add the following lines to my /etc/ssh/ssh_config
# KexAlgorithms diffie-hellman-group1-sha1,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1
# Ciphers 3des-cbc,blowfish-cbc,aes128-cbc,aes128-ctr,aes256-ctr
# regenerate keys with
#ssh-keygen -A
# restart ssh with

# service ssh restart
