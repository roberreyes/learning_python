device_list = ['R1' , 'R2' , 'S1']

#for device in device_list:
#    if device == 'R2':
#       continue
#   print(device)

for device in device_list:
    if device.startswith('R'):
        continue
    print(device)