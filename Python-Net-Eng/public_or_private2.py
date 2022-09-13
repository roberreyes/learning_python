ip = input("Please, enter an IP address: ")
octets = ip.split(".")
while not (len(octets) == 4 and octets[0].isnumeric() and octets[1].isnumeric() and octets[2].isnumeric() and octets[3].isnumeric() and int(octets[0]) >= 0 and int(octets[0]) <= 255 and int(octets[1]) >= 0 and int(octets[1]) <= 255 and int(octets[2]) >= 0 and int(octets[2]) <= 255 and int(octets[3]) >= 0 and int(octets[3]) <= 255):
    print("FAILED! Invalid IP address")
    ip = input("Please, enter an IP address: ")
    octets = ip.split(".")

for x in range(0,4,1):
    octets[x] = str(int(octets[x]))

def joining(list, sep):
    myip = sep.join(list)
    return myip

fullip = joining(octets, ".")
    
if octets[0] == "10":
    #Class A
    print(f"{fullip} is a class A private IP")

elif octets[0] == "172" and int(octets[1]) > 15 and int(octets[1]) < 32:
    #Class B
    print(f"{fullip} is a class B private IP")

elif octets[0] == "192" and octets[1] == "168":
    #Class C
    print(f"{fullip} is a class C private IP")
else:
    #Public
    print(f"{fullip} is not a private IP")