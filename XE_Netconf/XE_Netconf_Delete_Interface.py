from ncclient import manager
import xmltodict
import xml.dom.minidom

xe = {
    'host':'192.168.240.163',
    'port':'830',
    'username':'admin',
    'password':'cisco',
}
'''
IETF_INTERFACE_TYPES = {
        "loopback": "ianaift:softwareLoopback",
        "ethernet": "ianaift:ethernetCsmacd"
    }
'''
# Create an XML configuration template for ietf-interfaces

netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
        	<name>{name}</name>
        </interface>
    </interfaces>
</config>
"""


# Ask for the Interface Details to Add
new_loopback = {}
new_loopback["name"] = "Loopback" + raw_input("What loopback number to delete? ")

# Create the NETCONF data payload for this interface
netconf_data = netconf_interface_template.format(
        name = new_loopback["name"]
    )

print("The configuration payload to be sent over NETCONF.\n")
print(netconf_data)

print("Opening NETCONF Connection to {}".format(xe["host"]))

# Open a connection to the network device using ncclient
with manager.connect(host=xe['host'],
                     port=xe['port'],
                     username=xe['username'],
                     password=xe['password'],
                     hostkey_verify=False) as m:

    print("Sending a <edit-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.edit_config(netconf_data, target = 'running')

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
