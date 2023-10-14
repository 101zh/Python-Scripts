import math


def formatToAddress(ip: list):
    ipString = ""
    for num in range(4):
        ipString += str(ip[num])+"."
    ipString = ipString[:-1]
    return ipString


while True:
    while True:
        ipAddress = input("Give a valid IPv4 address: ")
        ipAddress = ipAddress.replace(" ", "")
        subnetMask = input("Give a valid Subnet Mask: ")
        subnetMask = subnetMask.replace(" ", "")

        binaryIP = ipAddress.split(".")
        binarySubnet = subnetMask.split(".")
        if len(binarySubnet) != 4 or len(binaryIP) != 4:
            print("\nPlease put in a valid IP/Subnet Mask")

        try:
            for i in range(4):
                binaryIP[i] = '{0:08b}'.format(int(binaryIP[i]))
                binarySubnet[i] = '{0:08b}'.format(int(binarySubnet[i]))
            break
        except ValueError:
            print("Please valid numbers in between the \".\"")

    binaryNetworkAddress = ["", "", "", ""]
    binaryBroadcastAddress = ["", "", "", ""]
    for i in range(4):
        subnetBits = binarySubnet[i]
        ipBits = binaryIP[i]
        for j in range(8):
            subnetBit = subnetBits[j:j+1]
            ipBit = ipBits[j:j+1]
            binaryNetworkAddress[i] += str(int(ipBit)*int(subnetBit))
            if (subnetBit == "1"):
                binaryBroadcastAddress[i] += ipBit
            else:
                binaryBroadcastAddress[i] += "1"

    networkAddress = [0]*4
    broadcastAddress = [0]*4
    totalNumOfHosts = 0
    for i in range(4):
        networkAddress[i] = int(binaryNetworkAddress[i], 2)
        broadcastAddress[i] = int(binaryBroadcastAddress[i], 2)
        # Counts the number of zeroes in a subnet mask
        totalNumOfHosts += binarySubnet[i].count("0")
    # 2^# of zeroes is how to find the total number of hosts
    totalNumOfHosts = math.pow(2, totalNumOfHosts)

    firstUsableAddress = networkAddress.copy()
    firstUsableAddress[3] += 1
    lastUsableAddress = broadcastAddress.copy()
    lastUsableAddress[3] -= 1

    print("_____________________________________________\n")
    print("IPv4 Address:                 | "+ipAddress)
    print("Subnet Mask:                  | "+subnetMask)
    print("Network Address:              | "+formatToAddress(networkAddress))
    print("Broadcast Address:            | "+formatToAddress(broadcastAddress))
    print("Range of Usable Host IPs:     | "+formatToAddress(firstUsableAddress) +
          " - "+formatToAddress(lastUsableAddress))
    print("Total Number of Hosts:        | "+str(totalNumOfHosts))
    print("Total Number of Usable Hosts: | "+str(totalNumOfHosts-2))
    print("Binary Subnet Mask:           | " + str(binaryIP))
    print("Binary IP address:            | "+str(binarySubnet))

    if (input("\nDo you want to exit this program? (y/n) ") == "y"):
        break
