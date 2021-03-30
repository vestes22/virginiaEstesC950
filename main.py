# Author: Virginia Estes
# Student ID: 000977601

import csv
from datetime import time, datetime
from package import Package
from packageHashTable import PackageHashTable
from MapGraph import Address
from MapGraph import MapGraph
from Truck import Truck

hashed_packages = PackageHashTable()
addresses = []
map = MapGraph()

# Parses addresses from WGUPS Distance Table.csv into the map object.
# O(N) time complexity, where N is the number of addresses.
with open('WGUPS Distance Table.csv') as addressFile:
    addressData = csv.reader(addressFile, delimiter=',')
    counter = 0
    for row in addressData:
        # Used to skip the parsing of the first row - the first row was not parsing correctly.
        if counter == 0:
            counter += 1
        # After we skip the first row, we parse the remaining rows into address objects.
        else:
            address = Address(int(row[0]), row[1], row[2], row[3], row[4])
            addresses.append(address)
            map.add_address(address)

# Adds the distances between addresses to the map.
map.add_bidirectional_distance(addresses[0], addresses[0], 0)
map.add_bidirectional_distance(addresses[0], addresses[1], 7.2)
map.add_bidirectional_distance(addresses[1], addresses[1], 0)
map.add_bidirectional_distance(addresses[0], addresses[2], 3.8)
map.add_bidirectional_distance(addresses[1], addresses[2], 7.1)
map.add_bidirectional_distance(addresses[2], addresses[2], 0)
map.add_bidirectional_distance(addresses[0], addresses[3], 11)
map.add_bidirectional_distance(addresses[1], addresses[3], 6.4)
map.add_bidirectional_distance(addresses[2], addresses[3], 9.2)
map.add_bidirectional_distance(addresses[3], addresses[3], 0)
map.add_bidirectional_distance(addresses[0], addresses[4], 2.2)
map.add_bidirectional_distance(addresses[1], addresses[4], 6.0)
map.add_bidirectional_distance(addresses[2], addresses[4], 4.4)
map.add_bidirectional_distance(addresses[3], addresses[4], 5.6)
map.add_bidirectional_distance(addresses[4], addresses[4], 0)
map.add_bidirectional_distance(addresses[0], addresses[5], 3.5)
map.add_bidirectional_distance(addresses[1], addresses[5], 4.8)
map.add_bidirectional_distance(addresses[2], addresses[5], 2.8)
map.add_bidirectional_distance(addresses[3], addresses[5], 6.9)
map.add_bidirectional_distance(addresses[4], addresses[5], 1.9)
map.add_bidirectional_distance(addresses[5], addresses[5], 0)
map.add_bidirectional_distance(addresses[0], addresses[6], 10.9)
map.add_bidirectional_distance(addresses[1], addresses[6], 1.6)
map.add_bidirectional_distance(addresses[2], addresses[6], 8.6)
map.add_bidirectional_distance(addresses[3], addresses[6], 8.6)
map.add_bidirectional_distance(addresses[4], addresses[6], 7.9)
map.add_bidirectional_distance(addresses[5], addresses[6], 6.3)
map.add_bidirectional_distance(addresses[6], addresses[6], 0)
map.add_bidirectional_distance(addresses[0], addresses[7], 8.6)
map.add_bidirectional_distance(addresses[1], addresses[7], 2.8)
map.add_bidirectional_distance(addresses[2], addresses[7], 6.3)
map.add_bidirectional_distance(addresses[3], addresses[7], 4.0)
map.add_bidirectional_distance(addresses[4], addresses[7], 5.1)
map.add_bidirectional_distance(addresses[5], addresses[7], 4.3)
map.add_bidirectional_distance(addresses[6], addresses[7], 4.0)
map.add_bidirectional_distance(addresses[7], addresses[7], 0)
map.add_bidirectional_distance(addresses[0], addresses[8], 7.6)
map.add_bidirectional_distance(addresses[1], addresses[8], 4.8)
map.add_bidirectional_distance(addresses[2], addresses[8], 5.3)
map.add_bidirectional_distance(addresses[3], addresses[8], 11.1)
map.add_bidirectional_distance(addresses[4], addresses[8], 7.5)
map.add_bidirectional_distance(addresses[5], addresses[8], 4.5)
map.add_bidirectional_distance(addresses[6], addresses[8], 4.2)
map.add_bidirectional_distance(addresses[7], addresses[8], 7.7)
map.add_bidirectional_distance(addresses[8], addresses[8], 0)
map.add_bidirectional_distance(addresses[0], addresses[9], 2.8)
map.add_bidirectional_distance(addresses[1], addresses[9], 6.3)
map.add_bidirectional_distance(addresses[2], addresses[9], 1.6)
map.add_bidirectional_distance(addresses[3], addresses[9], 7.3)
map.add_bidirectional_distance(addresses[4], addresses[9], 2.6)
map.add_bidirectional_distance(addresses[5], addresses[9], 1.5)
map.add_bidirectional_distance(addresses[6], addresses[9], 8.0)
map.add_bidirectional_distance(addresses[7], addresses[9], 9.3)
map.add_bidirectional_distance(addresses[8], addresses[9], 4.8)
map.add_bidirectional_distance(addresses[9], addresses[9], 0)
map.add_bidirectional_distance(addresses[0], addresses[10], 6.4)
map.add_bidirectional_distance(addresses[1], addresses[10], 7.3)
map.add_bidirectional_distance(addresses[2], addresses[10], 10.4)
map.add_bidirectional_distance(addresses[3], addresses[10], 1.0)
map.add_bidirectional_distance(addresses[4], addresses[10], 6.5)
map.add_bidirectional_distance(addresses[5], addresses[10], 8.7)
map.add_bidirectional_distance(addresses[6], addresses[10], 8.6)
map.add_bidirectional_distance(addresses[7], addresses[10], 4.6)
map.add_bidirectional_distance(addresses[8], addresses[10], 11.9)
map.add_bidirectional_distance(addresses[9], addresses[10], 9.4)
map.add_bidirectional_distance(addresses[10], addresses[10], 0)
map.add_bidirectional_distance(addresses[0], addresses[11], 3.2)
map.add_bidirectional_distance(addresses[1], addresses[11], 5.3)
map.add_bidirectional_distance(addresses[2], addresses[11], 3.0)
map.add_bidirectional_distance(addresses[3], addresses[11], 6.4)
map.add_bidirectional_distance(addresses[4], addresses[11], 1.5)
map.add_bidirectional_distance(addresses[5], addresses[11], 0.8)
map.add_bidirectional_distance(addresses[6], addresses[11], 6.9)
map.add_bidirectional_distance(addresses[7], addresses[11], 4.8)
map.add_bidirectional_distance(addresses[8], addresses[11], 4.7)
map.add_bidirectional_distance(addresses[9], addresses[11], 1.1)
map.add_bidirectional_distance(addresses[10], addresses[11], 7.3)
map.add_bidirectional_distance(addresses[11], addresses[11], 0)
map.add_bidirectional_distance(addresses[0], addresses[12], 7.6)
map.add_bidirectional_distance(addresses[1], addresses[12], 4.8)
map.add_bidirectional_distance(addresses[2], addresses[12], 5.3)
map.add_bidirectional_distance(addresses[3], addresses[12], 11.1)
map.add_bidirectional_distance(addresses[4], addresses[12], 7.5)
map.add_bidirectional_distance(addresses[5], addresses[12], 4.5)
map.add_bidirectional_distance(addresses[6], addresses[12], 4.2)
map.add_bidirectional_distance(addresses[7], addresses[12], 7.7)
map.add_bidirectional_distance(addresses[8], addresses[12], 0.6)
map.add_bidirectional_distance(addresses[9], addresses[12], 5.1)
map.add_bidirectional_distance(addresses[10], addresses[12], 12.0)
map.add_bidirectional_distance(addresses[11], addresses[12], 4.7)
map.add_bidirectional_distance(addresses[12], addresses[12], 0)
map.add_bidirectional_distance(addresses[0], addresses[13], 5.2)
map.add_bidirectional_distance(addresses[1], addresses[13], 3.0)
map.add_bidirectional_distance(addresses[2], addresses[13], 6.5)
map.add_bidirectional_distance(addresses[3], addresses[13], 3.9)
map.add_bidirectional_distance(addresses[4], addresses[13], 3.2)
map.add_bidirectional_distance(addresses[5], addresses[13], 3.9)
map.add_bidirectional_distance(addresses[6], addresses[13], 4.2)
map.add_bidirectional_distance(addresses[7], addresses[13], 1.6)
map.add_bidirectional_distance(addresses[8], addresses[13], 7.6)
map.add_bidirectional_distance(addresses[9], addresses[13], 4.6)
map.add_bidirectional_distance(addresses[10], addresses[13], 4.9)
map.add_bidirectional_distance(addresses[11], addresses[13], 3.5)
map.add_bidirectional_distance(addresses[12], addresses[13], 7.3)
map.add_bidirectional_distance(addresses[13], addresses[13], 0)
map.add_bidirectional_distance(addresses[0], addresses[14], 4.4)
map.add_bidirectional_distance(addresses[1], addresses[14], 4.6)
map.add_bidirectional_distance(addresses[2], addresses[14], 5.6)
map.add_bidirectional_distance(addresses[3], addresses[14], 4.3)
map.add_bidirectional_distance(addresses[4], addresses[14], 2.4)
map.add_bidirectional_distance(addresses[5], addresses[14], 3.0)
map.add_bidirectional_distance(addresses[6], addresses[14], 8.0)
map.add_bidirectional_distance(addresses[7], addresses[14], 3.3)
map.add_bidirectional_distance(addresses[8], addresses[14], 7.8)
map.add_bidirectional_distance(addresses[9], addresses[14], 3.7)
map.add_bidirectional_distance(addresses[10], addresses[14], 5.2)
map.add_bidirectional_distance(addresses[11], addresses[14], 2.6)
map.add_bidirectional_distance(addresses[12], addresses[14], 7.8)
map.add_bidirectional_distance(addresses[13], addresses[14], 1.3)
map.add_bidirectional_distance(addresses[14], addresses[14], 0)
map.add_bidirectional_distance(addresses[0], addresses[15], 3.7)
map.add_bidirectional_distance(addresses[1], addresses[15], 4.5)
map.add_bidirectional_distance(addresses[2], addresses[15], 5.8)
map.add_bidirectional_distance(addresses[3], addresses[15], 4.4)
map.add_bidirectional_distance(addresses[4], addresses[15], 2.7)
map.add_bidirectional_distance(addresses[5], addresses[15], 3.8)
map.add_bidirectional_distance(addresses[6], addresses[15], 5.8)
map.add_bidirectional_distance(addresses[7], addresses[15], 3.4)
map.add_bidirectional_distance(addresses[8], addresses[15], 6.6)
map.add_bidirectional_distance(addresses[9], addresses[15], 4.0)
map.add_bidirectional_distance(addresses[10], addresses[15], 5.4)
map.add_bidirectional_distance(addresses[11], addresses[15], 2.9)
map.add_bidirectional_distance(addresses[12], addresses[15], 6.6)
map.add_bidirectional_distance(addresses[13], addresses[15], 1.5)
map.add_bidirectional_distance(addresses[14], addresses[15], 0.6)
map.add_bidirectional_distance(addresses[15], addresses[15], 0)
map.add_bidirectional_distance(addresses[0], addresses[16], 7.6)
map.add_bidirectional_distance(addresses[1], addresses[16], 7.4)
map.add_bidirectional_distance(addresses[2], addresses[16], 5.7)
map.add_bidirectional_distance(addresses[3], addresses[16], 7.2)
map.add_bidirectional_distance(addresses[4], addresses[16], 1.4)
map.add_bidirectional_distance(addresses[5], addresses[16], 5.7)
map.add_bidirectional_distance(addresses[6], addresses[16], 7.2)
map.add_bidirectional_distance(addresses[7], addresses[16], 3.1)
map.add_bidirectional_distance(addresses[8], addresses[16], 7.2)
map.add_bidirectional_distance(addresses[9], addresses[16], 6.7)
map.add_bidirectional_distance(addresses[10], addresses[16], 8.1)
map.add_bidirectional_distance(addresses[11], addresses[16], 6.3)
map.add_bidirectional_distance(addresses[12], addresses[16], 7.2)
map.add_bidirectional_distance(addresses[13], addresses[16], 4.0)
map.add_bidirectional_distance(addresses[14], addresses[16], 6.4)
map.add_bidirectional_distance(addresses[15], addresses[16], 5.6)
map.add_bidirectional_distance(addresses[16], addresses[16], 0)
map.add_bidirectional_distance(addresses[0], addresses[17], 2.0)
map.add_bidirectional_distance(addresses[1], addresses[17], 6.0)
map.add_bidirectional_distance(addresses[2], addresses[17], 4.1)
map.add_bidirectional_distance(addresses[3], addresses[17], 5.3)
map.add_bidirectional_distance(addresses[4], addresses[17], 0.5)
map.add_bidirectional_distance(addresses[5], addresses[17], 1.9)
map.add_bidirectional_distance(addresses[6], addresses[17], 7.7)
map.add_bidirectional_distance(addresses[7], addresses[17], 5.1)
map.add_bidirectional_distance(addresses[8], addresses[17], 5.9)
map.add_bidirectional_distance(addresses[9], addresses[17], 2.3)
map.add_bidirectional_distance(addresses[10], addresses[17], 6.2)
map.add_bidirectional_distance(addresses[11], addresses[17], 1.2)
map.add_bidirectional_distance(addresses[12], addresses[17], 5.9)
map.add_bidirectional_distance(addresses[13], addresses[17], 3.2)
map.add_bidirectional_distance(addresses[14], addresses[17], 2.4)
map.add_bidirectional_distance(addresses[15], addresses[17], 1.6)
map.add_bidirectional_distance(addresses[16], addresses[17], 7.1)
map.add_bidirectional_distance(addresses[17], addresses[17], 0)
map.add_bidirectional_distance(addresses[0], addresses[18], 3.6)
map.add_bidirectional_distance(addresses[1], addresses[18], 5.0)
map.add_bidirectional_distance(addresses[2], addresses[18], 3.6)
map.add_bidirectional_distance(addresses[3], addresses[18], 6.0)
map.add_bidirectional_distance(addresses[4], addresses[18], 1.7)
map.add_bidirectional_distance(addresses[5], addresses[18], 1.1)
map.add_bidirectional_distance(addresses[6], addresses[18], 6.6)
map.add_bidirectional_distance(addresses[7], addresses[18], 4.6)
map.add_bidirectional_distance(addresses[8], addresses[18], 5.4)
map.add_bidirectional_distance(addresses[9], addresses[18], 1.8)
map.add_bidirectional_distance(addresses[10], addresses[18], 6.9)
map.add_bidirectional_distance(addresses[11], addresses[18], 1.0)
map.add_bidirectional_distance(addresses[12], addresses[18], 5.4)
map.add_bidirectional_distance(addresses[13], addresses[18], 3.0)
map.add_bidirectional_distance(addresses[14], addresses[18], 2.2)
map.add_bidirectional_distance(addresses[15], addresses[18], 1.7)
map.add_bidirectional_distance(addresses[16], addresses[18], 6.1)
map.add_bidirectional_distance(addresses[17], addresses[18], 1.6)
map.add_bidirectional_distance(addresses[18], addresses[18], 0)
map.add_bidirectional_distance(addresses[0], addresses[19], 6.5)
map.add_bidirectional_distance(addresses[1], addresses[19], 4.8)
map.add_bidirectional_distance(addresses[2], addresses[19], 4.3)
map.add_bidirectional_distance(addresses[3], addresses[19], 10.6)
map.add_bidirectional_distance(addresses[4], addresses[19], 6.5)
map.add_bidirectional_distance(addresses[5], addresses[19], 3.5)
map.add_bidirectional_distance(addresses[6], addresses[19], 3.2)
map.add_bidirectional_distance(addresses[7], addresses[19], 6.7)
map.add_bidirectional_distance(addresses[8], addresses[19], 1.0)
map.add_bidirectional_distance(addresses[9], addresses[19], 4.1)
map.add_bidirectional_distance(addresses[10], addresses[19], 11.5)
map.add_bidirectional_distance(addresses[11], addresses[19], 3.7)
map.add_bidirectional_distance(addresses[12], addresses[19], 1.0)
map.add_bidirectional_distance(addresses[13], addresses[19], 6.9)
map.add_bidirectional_distance(addresses[14], addresses[19], 6.8)
map.add_bidirectional_distance(addresses[15], addresses[19], 6.4)
map.add_bidirectional_distance(addresses[16], addresses[19], 7.2)
map.add_bidirectional_distance(addresses[17], addresses[19], 4.9)
map.add_bidirectional_distance(addresses[18], addresses[19], 4.4)
map.add_bidirectional_distance(addresses[19], addresses[19], 0)
map.add_bidirectional_distance(addresses[0], addresses[20], 1.9)
map.add_bidirectional_distance(addresses[1], addresses[20], 9.5)
map.add_bidirectional_distance(addresses[2], addresses[20], 3.3)
map.add_bidirectional_distance(addresses[3], addresses[20], 5.9)
map.add_bidirectional_distance(addresses[4], addresses[20], 3.2)
map.add_bidirectional_distance(addresses[5], addresses[20], 4.9)
map.add_bidirectional_distance(addresses[6], addresses[20], 11.2)
map.add_bidirectional_distance(addresses[7], addresses[20], 8.1)
map.add_bidirectional_distance(addresses[8], addresses[20], 8.5)
map.add_bidirectional_distance(addresses[9], addresses[20], 3.8)
map.add_bidirectional_distance(addresses[10], addresses[20], 6.9)
map.add_bidirectional_distance(addresses[11], addresses[20], 4.1)
map.add_bidirectional_distance(addresses[12], addresses[20], 8.5)
map.add_bidirectional_distance(addresses[13], addresses[20], 6.2)
map.add_bidirectional_distance(addresses[14], addresses[20], 5.3)
map.add_bidirectional_distance(addresses[15], addresses[20], 4.9)
map.add_bidirectional_distance(addresses[16], addresses[20], 10.6)
map.add_bidirectional_distance(addresses[17], addresses[20], 3.0)
map.add_bidirectional_distance(addresses[18], addresses[20], 4.6)
map.add_bidirectional_distance(addresses[19], addresses[20], 7.5)
map.add_bidirectional_distance(addresses[20], addresses[20], 0)
map.add_bidirectional_distance(addresses[0], addresses[21], 3.4)
map.add_bidirectional_distance(addresses[1], addresses[21], 10.9)
map.add_bidirectional_distance(addresses[2], addresses[21], 5.0)
map.add_bidirectional_distance(addresses[3], addresses[21], 7.4)
map.add_bidirectional_distance(addresses[4], addresses[21], 5.2)
map.add_bidirectional_distance(addresses[5], addresses[21], 6.9)
map.add_bidirectional_distance(addresses[6], addresses[21], 12.7)
map.add_bidirectional_distance(addresses[7], addresses[21], 10.4)
map.add_bidirectional_distance(addresses[8], addresses[21], 10.3)
map.add_bidirectional_distance(addresses[9], addresses[21], 5.8)
map.add_bidirectional_distance(addresses[10], addresses[21], 8.3)
map.add_bidirectional_distance(addresses[11], addresses[21], 6.2)
map.add_bidirectional_distance(addresses[12], addresses[21], 10.3)
map.add_bidirectional_distance(addresses[13], addresses[21], 8.2)
map.add_bidirectional_distance(addresses[14], addresses[21], 7.4)
map.add_bidirectional_distance(addresses[15], addresses[21], 6.9)
map.add_bidirectional_distance(addresses[16], addresses[21], 12.0)
map.add_bidirectional_distance(addresses[17], addresses[21], 5.0)
map.add_bidirectional_distance(addresses[18], addresses[21], 6.6)
map.add_bidirectional_distance(addresses[19], addresses[21], 9.3)
map.add_bidirectional_distance(addresses[20], addresses[21], 2.0)
map.add_bidirectional_distance(addresses[21], addresses[21], 0)
map.add_bidirectional_distance(addresses[0], addresses[22], 2.4)
map.add_bidirectional_distance(addresses[1], addresses[22], 8.3)
map.add_bidirectional_distance(addresses[2], addresses[22], 6.1)
map.add_bidirectional_distance(addresses[3], addresses[22], 4.7)
map.add_bidirectional_distance(addresses[4], addresses[22], 2.5)
map.add_bidirectional_distance(addresses[5], addresses[22], 4.2)
map.add_bidirectional_distance(addresses[6], addresses[22], 10.0)
map.add_bidirectional_distance(addresses[7], addresses[22], 7.8)
map.add_bidirectional_distance(addresses[8], addresses[22], 7.8)
map.add_bidirectional_distance(addresses[9], addresses[22], 4.3)
map.add_bidirectional_distance(addresses[10], addresses[22], 4.1)
map.add_bidirectional_distance(addresses[11], addresses[22], 3.4)
map.add_bidirectional_distance(addresses[12], addresses[22], 7.8)
map.add_bidirectional_distance(addresses[13], addresses[22], 5.5)
map.add_bidirectional_distance(addresses[14], addresses[22], 4.6)
map.add_bidirectional_distance(addresses[15], addresses[22], 4.2)
map.add_bidirectional_distance(addresses[16], addresses[22], 9.4)
map.add_bidirectional_distance(addresses[17], addresses[22], 2.3)
map.add_bidirectional_distance(addresses[18], addresses[22], 3.9)
map.add_bidirectional_distance(addresses[19], addresses[22], 6.8)
map.add_bidirectional_distance(addresses[20], addresses[22], 2.9)
map.add_bidirectional_distance(addresses[21], addresses[22], 4.4)
map.add_bidirectional_distance(addresses[22], addresses[22], 0)
map.add_bidirectional_distance(addresses[0], addresses[23], 6.4)
map.add_bidirectional_distance(addresses[1], addresses[23], 6.9)
map.add_bidirectional_distance(addresses[2], addresses[23], 9.7)
map.add_bidirectional_distance(addresses[3], addresses[23], 0.6)
map.add_bidirectional_distance(addresses[4], addresses[23], 6.0)
map.add_bidirectional_distance(addresses[5], addresses[23], 9.0)
map.add_bidirectional_distance(addresses[6], addresses[23], 8.2)
map.add_bidirectional_distance(addresses[7], addresses[23], 4.2)
map.add_bidirectional_distance(addresses[8], addresses[23], 11.5)
map.add_bidirectional_distance(addresses[9], addresses[23], 7.8)
map.add_bidirectional_distance(addresses[10], addresses[23], 0.4)
map.add_bidirectional_distance(addresses[11], addresses[23], 6.9)
map.add_bidirectional_distance(addresses[12], addresses[23], 11.5)
map.add_bidirectional_distance(addresses[13], addresses[23], 4.4)
map.add_bidirectional_distance(addresses[14], addresses[23], 4.8)
map.add_bidirectional_distance(addresses[15], addresses[23], 5.6)
map.add_bidirectional_distance(addresses[16], addresses[23], 7.5)
map.add_bidirectional_distance(addresses[17], addresses[23], 5.5)
map.add_bidirectional_distance(addresses[18], addresses[23], 6.5)
map.add_bidirectional_distance(addresses[19], addresses[23], 11.4)
map.add_bidirectional_distance(addresses[20], addresses[23], 6.4)
map.add_bidirectional_distance(addresses[21], addresses[23], 7.9)
map.add_bidirectional_distance(addresses[22], addresses[23], 4.5)
map.add_bidirectional_distance(addresses[23], addresses[23], 0)
map.add_bidirectional_distance(addresses[0], addresses[24], 2.4)
map.add_bidirectional_distance(addresses[1], addresses[24], 10.0)
map.add_bidirectional_distance(addresses[2], addresses[24], 6.1)
map.add_bidirectional_distance(addresses[3], addresses[24], 6.4)
map.add_bidirectional_distance(addresses[4], addresses[24], 4.2)
map.add_bidirectional_distance(addresses[5], addresses[24], 5.9)
map.add_bidirectional_distance(addresses[6], addresses[24], 11.7)
map.add_bidirectional_distance(addresses[7], addresses[24], 9.5)
map.add_bidirectional_distance(addresses[8], addresses[24], 9.5)
map.add_bidirectional_distance(addresses[9], addresses[24], 4.8)
map.add_bidirectional_distance(addresses[10], addresses[24], 4.9)
map.add_bidirectional_distance(addresses[11], addresses[24], 5.2)
map.add_bidirectional_distance(addresses[12], addresses[24], 9.5)
map.add_bidirectional_distance(addresses[13], addresses[24], 7.2)
map.add_bidirectional_distance(addresses[14], addresses[24], 6.3)
map.add_bidirectional_distance(addresses[15], addresses[24], 5.9)
map.add_bidirectional_distance(addresses[16], addresses[24], 11.1)
map.add_bidirectional_distance(addresses[17], addresses[24], 4.0)
map.add_bidirectional_distance(addresses[18], addresses[24], 5.6)
map.add_bidirectional_distance(addresses[19], addresses[24], 8.5)
map.add_bidirectional_distance(addresses[20], addresses[24], 2.8)
map.add_bidirectional_distance(addresses[21], addresses[24], 3.4)
map.add_bidirectional_distance(addresses[22], addresses[24], 1.7)
map.add_bidirectional_distance(addresses[23], addresses[24], 5.4)
map.add_bidirectional_distance(addresses[24], addresses[24], 0)
map.add_bidirectional_distance(addresses[0], addresses[25], 5.0)
map.add_bidirectional_distance(addresses[1], addresses[25], 4.4)
map.add_bidirectional_distance(addresses[2], addresses[25], 2.8)
map.add_bidirectional_distance(addresses[3], addresses[25], 10.1)
map.add_bidirectional_distance(addresses[4], addresses[25], 5.4)
map.add_bidirectional_distance(addresses[5], addresses[25], 3.5)
map.add_bidirectional_distance(addresses[6], addresses[25], 5.1)
map.add_bidirectional_distance(addresses[7], addresses[25], 6.2)
map.add_bidirectional_distance(addresses[8], addresses[25], 2.8)
map.add_bidirectional_distance(addresses[9], addresses[25], 3.2)
map.add_bidirectional_distance(addresses[10], addresses[25], 11.0)
map.add_bidirectional_distance(addresses[11], addresses[25], 3.7)
map.add_bidirectional_distance(addresses[12], addresses[25], 2.8)
map.add_bidirectional_distance(addresses[13], addresses[25], 6.4)
map.add_bidirectional_distance(addresses[14], addresses[25], 6.5)
map.add_bidirectional_distance(addresses[15], addresses[25], 5.7)
map.add_bidirectional_distance(addresses[16], addresses[25], 6.2)
map.add_bidirectional_distance(addresses[17], addresses[25], 5.1)
map.add_bidirectional_distance(addresses[18], addresses[25], 4.3)
map.add_bidirectional_distance(addresses[19], addresses[25], 1.8)
map.add_bidirectional_distance(addresses[20], addresses[25], 6.0)
map.add_bidirectional_distance(addresses[21], addresses[25], 7.9)
map.add_bidirectional_distance(addresses[22], addresses[25], 6.8)
map.add_bidirectional_distance(addresses[23], addresses[25], 10.6)
map.add_bidirectional_distance(addresses[24], addresses[25], 7.0)
map.add_bidirectional_distance(addresses[25], addresses[25], 0)
map.add_bidirectional_distance(addresses[0], addresses[26], 3.6)
map.add_bidirectional_distance(addresses[1], addresses[26], 13.0)
map.add_bidirectional_distance(addresses[2], addresses[26], 7.4)
map.add_bidirectional_distance(addresses[3], addresses[26], 10.1)
map.add_bidirectional_distance(addresses[4], addresses[26], 5.5)
map.add_bidirectional_distance(addresses[5], addresses[26], 7.2)
map.add_bidirectional_distance(addresses[6], addresses[26], 14.2)
map.add_bidirectional_distance(addresses[7], addresses[26], 10.7)
map.add_bidirectional_distance(addresses[8], addresses[26], 14.1)
map.add_bidirectional_distance(addresses[9], addresses[26], 6.0)
map.add_bidirectional_distance(addresses[10], addresses[26], 6.8)
map.add_bidirectional_distance(addresses[11], addresses[26], 6.4)
map.add_bidirectional_distance(addresses[12], addresses[26], 14.1)
map.add_bidirectional_distance(addresses[13], addresses[26], 10.5)
map.add_bidirectional_distance(addresses[14], addresses[26], 8.8)
map.add_bidirectional_distance(addresses[15], addresses[26], 8.4)
map.add_bidirectional_distance(addresses[16], addresses[26], 13.6)
map.add_bidirectional_distance(addresses[17], addresses[26], 5.2)
map.add_bidirectional_distance(addresses[18], addresses[26], 6.9)
map.add_bidirectional_distance(addresses[19], addresses[26], 13.1)
map.add_bidirectional_distance(addresses[20], addresses[26], 4.1)
map.add_bidirectional_distance(addresses[21], addresses[26], 4.7)
map.add_bidirectional_distance(addresses[22], addresses[26], 3.1)
map.add_bidirectional_distance(addresses[23], addresses[26], 7.8)
map.add_bidirectional_distance(addresses[24], addresses[26], 1.3)
map.add_bidirectional_distance(addresses[25], addresses[26], 8.3)
map.add_bidirectional_distance(addresses[26], addresses[26], 0.0)

# Parses the package data from WGUPS Package File.csv into package objects and adds them to our package hash table.
# O(P * A) time complexity, where P is the number of packages and A is the number of addresses.
with open('WGUPS Package File.csv') as packageFile:
    packageData = csv.reader(packageFile, delimiter=',')
    counter = 0

    for row in packageData:
        # Used to skip the parsing of the first row - the first row was not parsing correctly.
        if counter == 0:
            counter += 1
        # After we skip the first row, we parse each remaining row into a package object.
        else:
            # Compares the package delivery address to the addresses in our map.
            # If a match is found, it assigns the package an Address ID to the corresponding address object in the map.
            # This allows access to distances between addresses stored in our map.
            package_address_id = -1
            for address in addresses:
                if address.get_street() == row[1]:
                    package_address_id = address.get_address_id()

            # Creates a package object from each row of data, and inserts it into the package hash table.
            package = Package(int(row[0]), package_address_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            starting_time = datetime(2021, 12, 31, 7, 59, 0, 0)
            package.update_status(starting_time, "At Hub")
            hashed_packages.insert_package(package)
            #status = hashed_packages.search(package.get_package_id()).get_status(starting_time)
            #print(str(status[0].time()) + status[1])
            #print(package.get_address())
            #print("Address ID: " + str(package.get_address_id()))
            #print(row)

# Updates the address for package 9 to the correct address.
hashed_packages.search(9).set_address_id(19)

# A function that takes a Truck object as input, and delivers the packages loaded on that truck.
# Delivery is based on the "Nearest Neighbor" principle. The next package for delivery is determined
# based on which delivery address is closest to the truck's current address.
# O(N^2) time complexity, where N is the number of packages.
def deliver_packages(truck):
    # While there are still packages left on the truck, deliver them.
    while len(truck.get_packages()) > 0:

        # The shortest distance to the next delivery (so far) is initialized to the distance between
        # the truck and the first delivery address on its list.
        shortest_distance = map.get_distance(addresses[truck.get_current_address()],
                                             addresses[hashed_packages.search(truck.get_package(0)).get_address_id()])

        index = 0  # Keeps track of which package we are currently working with in in the iteration.

        # Iterates through each package loaded on the truck and examines the distances to each of them.
        # If a shorter distance is found, we update the shortest_distance and next_delivery_index variables.
        for package in truck.get_packages():
            distance = map.get_distance(addresses[truck.get_current_address()],
                                        addresses[hashed_packages.search(package).get_address_id()])

            if distance < shortest_distance:
                shortest_distance = distance
                truck.get_packages().insert(0, truck.get_packages().pop(index))

            index += 1

        # Now that the closest delivery address has been identified, we "deliver" that package.
        # We do that by:
        #   1) Driving to that address (adding the distance, in miles, to the truck and updating the truck's
        #      current address attribute).
        #   2) Determining the time of delivery by calculating the seconds it took to drive to the delivery address
        #      and adding them to the truck's "clock" or timer.
        #   3) Updating the status of the package to "Delivered" along with the time of delivery.
        #   4) Removing the package from the truck.
        delivered_package = truck.get_package(0)
        truck.set_current_address(hashed_packages.search(delivered_package).get_address_id())
        truck.add_miles(shortest_distance)
        seconds_driven = int((shortest_distance/truck.get_miles_per_hour()) * 3600)
        truck.add_seconds(seconds_driven)
        delivery_time = truck.get_timer()
        hashed_packages.search(delivered_package).update_status(delivery_time, "Delivered")
        truck.remove_package(0)


# Instantiate our truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

# Packages loaded onto a truck are managed via an array. See the Truck class for more details.
truck2.load(1)
truck2.load(13)
truck2.load(14)
truck2.load(15)
truck2.load(16)
truck2.load(20)
truck2.load(29)
truck2.load(30)
truck2.load(31)
truck2.load(34)
truck2.load(37)
truck2.load(40)
truck2.load(19)
truck2.load(21)
truck2.load(32)
truck2.load(38)

truck1.load(6)
truck1.load(25)
truck1.load(26)
truck1.load(2)
truck1.load(4)
truck1.load(5)
truck1.load(7)
truck1.load(10)

# The trucks start their day at the hub.
AT_HUB = 0
truck1.set_current_address(AT_HUB)
truck2.set_current_address(AT_HUB)

# Truck 2 is leaving the hub at 8:00AM. Truck 1 won't leave the hub until 9:05 to take care of the delayed packages.
# Each truck uses a timer (a datetime object) to keep track of what time their packages are delivered.
truck2_new_time = datetime(2021, 12, 31, 8, 0, 00)
truck1_new_time = datetime(2021, 12, 31, 9, 5, 00)
truck2.set_timer(truck2_new_time)
truck1.set_timer(truck1_new_time)
truck1_packages = truck1.get_packages()
truck2_packages = truck2.get_packages()

# For each package in Truck 2, we need to update the status of the package to reflect that it is on the way.
# O(N) time complexity, where N is the number of packages on the truck.
for each_package in truck2_packages:
    hashed_packages.search(each_package).update_status(truck2_new_time, "En Route - On Truck 2")

# For each package in Truck 1, we need to update the status of the package to reflect that it is on the way.
for each_package in truck1_packages:
    hashed_packages.search(each_package).update_status(truck1_new_time, "En Route - On Truck 1")

# Now we call our delivery algorithm.
deliver_packages(truck2)
deliver_packages(truck1)

# Truck 1 and Truck 2 have delivered their loads, but we still have packages remaining.
# Truck 2 will return to the hub and take care of the rest of the packages.
# We first find out how far away from the hub Truck 2 is and add that distance to its miles driven attribute.
# We also calculate how long (in seconds) it will take to return to the hub so we can update
# the truck's timer.
distance_from_hub = map.get_distance(addresses[truck2.get_current_address()], addresses[0])
truck2.add_miles(distance_from_hub)
hours_driven = distance_from_hub / truck2.get_miles_per_hour()
hours_to_seconds = int(hours_driven * 3600)
truck2.add_seconds(hours_to_seconds)
truck2.set_current_address(0)

# We load the rest of the packages onto Truck 2.
truck2.load(3)
truck2.load(8)
truck2.load(9)
truck2.load(11)
truck2.load(12)
truck2.load(17)
truck2.load(18)
truck2.load(22)
truck2.load(23)
truck2.load(24)
truck2.load(27)
truck2.load(28)
truck2.load(33)
truck2.load(35)
truck2.load(36)
truck2.load(39)

# We update the status for each package so they reflect the time they loaded and their status.
for each_package in truck2_packages:
    hashed_packages.search(each_package).update_status(truck2.get_timer(), "En Route - On Truck 2")

deliver_packages(truck2)

print("Truck 2 Miles Driven: " + str(truck2.get_miles_driven()))
print("Truck 2 final delivery time: " + str(truck2.get_timer().time()))
print("Truck 1 Miles Driven: " + str(truck1.get_miles_driven()))
print("Truck 1 final delivery time: " + str(truck1.get_timer().time()))
print("Total Miles Driven: " + str(truck2.get_miles_driven() + truck1.get_miles_driven()))
print("Final Delivery Made: " + str(truck2.get_timer().time()))
print("\n")

# -----------------------------------------------------------------------------------------------
#   USER INTERFACE
# -----------------------------------------------------------------------------------------------

# Function to display the status of each package at a certain time.
#
def package_statuses():
    # Prompts user to enter a time (in military time).
    hour = input("Please enter the 2 digit hour: ")
    minute = input("Please enter the 2 digit minute: ")
    print("Here is the status of each package at " + str(hour) + ":" + str(minute))

    # Stores the time the user entered as a datetime object. This allows us to compare the time the user entered
    # to the timestamps associated with each package status.
    user_datetime = datetime(2021, 12, 31, int(hour), int(minute), 0, 0)
    print(user_datetime)

    # Iterates through all packages in the hash table, finds the status of each package at the time the user
    # entered, and displays the status for the user.
    # Time complexity of O(N * S), where N is the number of packages, and S is the number of times
    # the status of the package has been updated.
    package_id = 1
    while package_id < 41:
        # Status changes for each package are stored in a 2D array. Retrieve that first.
        all_package_statuses = hashed_packages.search(package_id).get_all_statuses()
        index = 0
        current_status = 0
        # Iterate through each status update for that package. Compare the timestamp of the update to the time the
        # user entered. Return and display the status of the package for the user's specified time.
        for status in all_package_statuses:
            if status[0] < user_datetime:
                current_status = index
            index +=1
        print("As of " + str(all_package_statuses[current_status][0].time()) + ", Package " + str(package_id) + " was " + str(all_package_statuses[current_status][1]))
        package_id += 1
    # Before we exit the program, let's see if the user wants to do anything else.
    user_input = input("Press A to enter a different time. \n"
                       "Press B to return to the main menu. \n"
                       "Press any other key to exit.")
    if user_input == 'A' or user_input == 'a':
        package_statuses()
    elif user_input == 'B' or user_input == 'b':
        main_menu()

# A function to display the details of a specific package based on package ID.
# O(S) time complexity, where S is the number status updates for the package.
def package_details():
    package_id = input("Please enter the Package ID: \n")
    package = hashed_packages.search(int(package_id))
    print("Package ID: " + str(package.get_package_id()))
    print("Delivery Address: " + package.get_address())
    print("Delivery Deadline: " + package.get_deadline())
    print("Delivery City: " + package.get_city())
    print("Delivery Zip Code: " + package.get_zip())
    print("Package Weight: " + package.get_weight())
    print("Special Notes: " + package.get_special_notes() + "\n")
    print("Package Status History: ")
    package_status = package.get_all_statuses()
    index = 0
    for status in package_status:
        print("Time: " + str(package_status[index][0].time()) + " Status: " + str(package_status[index][1]))
        index += 1

    # Before we exit the program, let's see if the user wants to do anything else.
    user_input = input("\nPress A to enter a different Package ID. \n"
                       "Press B to return to the main menu. \n"
                       "Press any other key to exit.")
    if user_input == 'a' or user_input == "A":
        package_details()
    elif user_input == 'b' or user_input == 'B':
        main_menu()

# A function to display the main menu for the user interface.
def main_menu():
    user_answer = input("Please make a selection: \n"
                        + "    Press A to view package details by Package ID. \n"
                        + "    Press B to view package statuses by time. \n"
                        + "    Press any other key to Exit.")
    if user_answer == 'A' or user_answer == 'a':
        package_details()
    elif user_answer == 'B' or user_answer == 'b':
        package_statuses()

main_menu()