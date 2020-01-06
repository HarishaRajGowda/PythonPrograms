import ipaddress
IPv4_Subnet = '172.16.0.0/27'
IPv6_Subnet = '2002::/126'

''' IPv4 Loop '''
print('IP4 hosts:')
ipv4 = ipaddress.IPv4Network(IPv4_Subnet)

print('Subnet:'.format(ipv4))
print('Subnet mask:'.format(ipv4.netmask))
print('No. Of Valid Hosts:'.format(ipv4.num_addresses))

''' IPv6 Host '''
print('IPv6 hosts:')
ipv6 = ipaddress.IPv6Network(IPv6_Subnet)
