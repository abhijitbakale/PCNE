from ncclient import manager

xe = {
    'host': '192.168.240.163',
    'port': '830',
    'username': 'admin',
    'password': 'cisco'
}


with manager.connect(host = xe['host'], port = xe['port'], username = xe['username'], password = xe['password'], hostkey_verify = False) as m:
    for capability in m.server_capabilities:
        print capability
