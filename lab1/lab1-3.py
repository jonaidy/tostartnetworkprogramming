import napalm
from pprint import pprint


driver = napalm.get_network_driver('ios')
device = driver(
    hostname= "sandbox-iosxe-recomm-1.cisco.com",
    username= "developer",
    password= "C1sco12345",
    optional_args={"port":22},
)
device.open()
alive = device.is_alive()
if alive['is_alive'] is True:
    print(f'{device.hostname} is alive!')
    config = device.get_config()
    interface_ip = device.get_interfaces_ip()
    arp_table = device.get_arp_table()
    pprint(config)
    pprint(interface_ip)
    pprint(arp_table)
else:
    print(f'{device.hostname} is not accessible!')

device.close()