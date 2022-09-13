my_ip_addresses = ["192.168.1.1", "172.30.249.2", "172.98.144.254", "10.0.0.1", "45.12.23.21", "12.32.123.32"]
my_public_ips = []
my_private_ips = []


for my_ips in my_ip_addresses:
    #Class A
    if my_ips[0:2] == "10":
        my_private_ips.append(my_ips)
    #Class B
    elif my_ips[0:3] == "172" and int(my_ips[4:6]) > 15 and int(my_ips[4:6]) < 32:
        my_private_ips.append(my_ips)
    #Class C
    elif my_ips[0:7] == "192.168":
        my_private_ips.append(my_ips)

    else:
        my_public_ips.append(my_ips)

print(f"My private IPs are {my_private_ips}")
print(f"My public IPs are {my_public_ips}")

