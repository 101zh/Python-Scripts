ipAddress = input("Give a valid IPv4 address: ")
ipAddress = ipAddress.replace(" ", "")
subnetMask = input("Give a valid Subnet Mask: ")
subnetMask = subnetMask.replace(" ", "")

tempIp = ipAddress.split(".")
tempSubnetMask = subnetMask.split(".")

binaryIP = [0, 0, 0, 0]
binarySubnet = [0, 0, 0, 0]
for i in range(4):
    binaryIP[i] = '{0:08b}'.format(int(tempIp[i]))
    binarySubnet[i] = '{0:08b}'.format(int(tempSubnetMask[i]))

print(binaryIP)
print(binarySubnet)

