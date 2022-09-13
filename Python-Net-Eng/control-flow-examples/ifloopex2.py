vendor = input("Please select your vendor: ")
vendor = vendor.lower()

if vendor == "cisco":
    print("You have selected Cisco")
    
elif vendor == "fortinet":
    print("You have selected Fortinet")

elif vendor == "vmware":
    print("You have selected VMWare")

elif vendor == "meraki":
    print("You have selected Meraki")

else:
    print("Unrecognized vendor")
