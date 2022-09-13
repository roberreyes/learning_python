protocols = ['EIGRP', 'OSPF', 'RIP', 'ISIS']

if 'BGP' not in protocols:
    print('There is no path vector protocols')
else:
    print('There is a path vector protocol')
