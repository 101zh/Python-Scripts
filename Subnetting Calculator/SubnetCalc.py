ipAddress = input("Give a valid IPv4 address: ")
ipAddress = ipAddress.replace(" ", "")

tempIp = ipAddress.split(".")
binaryIP = [0, 0, 0, 0]
for i in range(4):
    binaryIP[i] = '{0:08b}'.format(int(tempIp[i]))


