import ipaddress
IPv4_Subnet = '192.168.100.0/27'
IPv6_Subnet = '2001::/125'

''' IPv4 Loop '''
print('IP4 hosts:')
for ipv4 in ipaddress.IPv4Network(IPv4_Subnet).hosts():
    print(ipv4)

''' IPv6 Host '''
print('IPv6 hosts:')
for ipv6 in ipaddress.IPv6Network(IPv6_Subnet).hosts():
    print(ipv6)
