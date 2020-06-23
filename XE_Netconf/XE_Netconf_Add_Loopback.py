from ncclient import manager
import xml.dom.minidom

xe = {
    'host':'192.168.240.164',
    'port':'830',
    'username':'admin',
    'password':'cisco'
}

IETF_INTERFACE_TYPES = {
    "loopback":"ianaift:softwareLoopback",
    'ethernet':'ianaift:ethernetCsmacd'
}


# Create an XML configuration template for ietf-interface
netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        	<name>{name}</name>
        	<description>{desc}</description>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                {type}
            </type>
        	<enabled>{status}</enabled>
        	<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        		<address>
        			<ip>{ip_address}</ip>
        			<netmask>{mask}</netmask>
        		</address>
        	</ipv4>
        </interface>
    </interfaces>
</config>"""

# Ask for the Interface Details to Add

new_loopback = {}
new_loopback['name'] = "Loopback" + raw_input("Enter the Loopback Interface Number: ")
new_loopback['desc'] = raw_input("Enter the description for the Loopback Interface: ")
new_loopback['type'] = IETF_INTERFACE_TYPES["loopback"]
new_loopback['status'] = "true"
new_loopback['ip_address'] = raw_input("Enter IP address for the Loopback Interface: ")
new_loopback['mask'] = raw_input("Enter Subnet Mask for the Loopback Interface: ")

# Create the NETCONF data payload for this interface

netconf_data = netconf_interface_template.format(
    name=new_loopback['name'],
    desc=new_loopback['desc'],
    type=new_loopback['type'],
    status=new_loopback['status'],
    ip_address=new_loopback['ip_address'],
    mask=new_loopback['mask']
)


with manager.connect(host=xe['host'],
                     port=xe['port'],
                     username=xe['username'],
                     password=xe['password'],
                     hostkey_verify=False) as m:

    netconf_reply = m.edit_config(netconf_data, target = 'running')

    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

