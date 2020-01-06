import ipaddress
IPv4_Subnet = '172.16.0.0/27'
IPv6_Subnet = '2002::/126'


print('IP4 Subnet:')
ipv4 = ipaddress.IPv4Network(IPv4_Subnet)

sub = str(ipv4)
netmask = str(ipv4.netmask)
num_addresses = str(ipv4.num_addresses)

print('Subnet:'.format(sub))
print('Subnet mask:'.format(netmask))
print('No. Of Valid Hosts:'.format(num_addresses))

''' IPv6 Host '''
print('IPv6 Subnet:')
ipv6 = ipaddress.IPv6Network(IPv6_Subnet)

sub = str(ipv6)
netmask = str(ipv6.netmask)
num_addresses = str(ipv6.num_addresses)

print('Subnet:'.format(sub))
print('Subnet mask:'.format(netmask))
print('No. Of Valid Hosts:'.format(num_addresses))

