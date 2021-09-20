from os import X_OK
import ipaddress

IP = '192.168.0.0'
MASK = '255.255.0.0'
CIDR='24'


host = ipaddress.IPv4Address(IP)
net = ipaddress.IPv4Network(IP + '/' + MASK, False)
print('IP:', IP)
print('Mask:', MASK)
print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast:', net.broadcast_address)

