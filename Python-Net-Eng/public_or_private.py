ip = input("Please, enter an IP address: ")
octets = ip.split(".")

if len(octets) == 4 and octets[0].isnumeric() and octets[1].isnumeric() and octets[2].isnumeric() and octets[3].isnumeric() and int(octets[0]) >= 0 and int(octets[0]) <= 255 and int(octets[1]) >= 0 and int(octets[1]) <= 255 and int(octets[2]) >= 0 and int(octets[2]) <= 255 and int(octets[3]) >= 0 and int(octets[3]) <= 255:
    
    octets[0] = str(int(octets[0]))
    octets[1] = str(int(octets[1]))
    octets[2] = str(int(octets[2]))
    octets[3] = str(int(octets[3]))

    #Class A
    if octets[0] == "10":
        fullip = octets[0]+"."+octets[1]+"."+octets[2]+"."+octets[3]
        print(f"{fullip} is a class A private IP")
    #Class B
    elif octets[0] == "172" and int(octets[1]) > 15 and int(octets[1]) < 32:
        fullip = octets[0]+"."+octets[1]+"."+octets[2]+"."+octets[3]
        print(f"{fullip} is a class B private IP")
    #Class C
    elif octets[0] == "192" and octets[1] == "168":
        fullip = octets[0]+"."+octets[1]+"."+octets[2]+"."+octets[3]
        print(f"{fullip} is a class C private IP")

    else:
        fullip = octets[0]+"."+octets[1]+"."+octets[2]+"."+octets[3]
        print(f"{fullip} is a not a private IP")

else:
    print("Please, enter a valid IP")
