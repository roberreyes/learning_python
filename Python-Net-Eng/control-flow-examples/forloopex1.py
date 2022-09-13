interfaces = ["interface Gi0/0/0.75", "interface Gi0/0/0.100", "interface Tunnel40443", "interface Loopback40443"]
for inter in interfaces:
    print(f"{inter}\n ip authentication mode eigrp 40443 md5\n")
    