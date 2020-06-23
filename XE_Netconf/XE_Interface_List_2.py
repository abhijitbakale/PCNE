from ncclient import manager
import xmltodict
import xml.dom.minidom

xe = {
    'host': '192.168.240.164',
    'port': '830',
    'username': 'admin',
    'password': 'cisco'
}

netconf_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet1</name>
        </interface>
    </interfaces>
</filter>
"""

with manager.connect(host=xe['host'],
                     port=xe['port'],
                     username=xe['username'],
                     password=xe['password'],
                     hostkey_verify=False) as m:
    netconf_reply = m.get_config(source='running', filter=netconf_filter)
    print xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()

netconf_data = xmltodict.parse(netconf_reply.xml)['rpc-reply']['data']

interfaces = netconf_data['interfaces']['interface']

for interface in interfaces:
    print "Interface {} enabled status is {}".format(
        interface['name'],
        interface['enabled']
    )