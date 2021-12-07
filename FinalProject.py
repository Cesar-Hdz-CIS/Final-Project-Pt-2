# Cesar Hernandez
# 1835494

import csv
from operator import itemgetter

mfl = []  # Creating Blank List for Manufacturers
prl = []  # Creating Blank list for Prices
sdl = []  # Creating Blank List for Service Date

# Opening Each CSV File and Appending to empty lists
with open('ManufacturerList.csv') as manlist:
    ml = csv.reader(manlist)
    for line in ml:
        mfl.append(line)

with open('PriceList.csv') as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        prl.append(line)

with open('ServiceDatesList.csv') as sdlist:
    sl = csv.reader(sdlist)
    for line in sl:
        sdl.append(line)

# Sorting into a new list by order ID
new_mfl = (sorted(mfl, key=itemgetter(0)))
new_prl = (sorted(prl, key=itemgetter(0)))
new_sdl = (sorted(sdl, key=itemgetter(0)))

# Appending Prices and Service dates together with Manufacturers
for x in range(0, len(new_mfl)):
    new_mfl[x].append(prl[x][1])

for x in range(0, len(new_mfl)):
    new_mfl[x].append(sdl[x][1])

# Create the final list
final_list = new_mfl
# Sort final list
full_inventory = (sorted(final_list, key=itemgetter(1)))

# Create new CSV file with a full inventory
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)
    for x in range(0, len(full_inventory)):
        fiwrite.writerow(full_inventory[x])

# Creating empty lists for the item types Ex: Laptop, Phone, etc.
item_type = final_list
tower_list = []
laptop_list = []
phone_list = []

# Appending to the lists depending on the item type
for x in range(0, len(item_type)):
    if item_type[x][2] == 'tower':
        tower_list.append(item_type[x])
    elif item_type[x][2] == 'phone':
        phone_list.append(item_type[x])
    elif item_type[x][2] == 'laptop':
        laptop_list.append(item_type[x])

# Creating new CSV files for each item type
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)
    for x in range(0, len(laptop_list)):
        liwrite.writerow(laptop_list[x])
with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)
    for x in range(0, len(phone_list)):
        piwrite.writerow(phone_list[x])
with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)
    for x in range(0, len(tower_list)):
        tiwrite.writerow(tower_list[x])

# Creating blank damage list
damagelist = []

# Appending to damage list for each item which is damaged
for x in range(0, len(item_type)):
    if item_type[x][3] == 'damaged':
        damagelist.append(item_type[x])
damagelist = (sorted(damagelist, key=itemgetter(4), reverse=True))

# Creating CSV file for demaged items
with open('DamageInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)
    for x in range(0, len(damagelist)):
        diwrite.writerow(damagelist[x])

user_manu = str()

# Creating menu for users to input in order to find requested item
while user_manu != 'q':
    user_manu = str(input('Please Enter Manufacturer, or type "q" to exit: \n'))
    user_type = str(input('Please Enter Item Type: \n'))
    your_item = []
    for x in range(0, len(final_list)):
        if user_manu != 'q' and user_manu in final_list[x] and user_type in final_list[x]:
            your_item.append(final_list[x])
    if len(your_item) != 0 and user_manu != 'q':
        your_item = sorted(your_item, key=itemgetter(4), reverse=True)
        print('Your item is:', your_item[0])
        print('You may, also, consider:', )
    else:
        print ('No such item in inventory')

    # user_manu=str(input("Please Enter Manufacturer, or type 'q' to quit: \n"))
    # user_type=str(input('Please enter item type: \n'))
