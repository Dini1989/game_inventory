#The given inventories

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


#Display inventory function

def display_inventory():

    print("Inventory:")
    for item in inv.items():
        print (item[1], item[0])
    print("Total number of items:", sum(inv.values()))


#Loot adding function

def add_to_inventory(inventory, added_items):

   for i in added_items:
        inventory[i] = inventory.get(i, 0) + 1


#Sorting function

def print_table(order=None):

    if order == None:
        sorted_inv = inv.items()
    elif order == "count,asc":
        sorted_inv = sorted(inv.items(), key=lambda item: item[1])
    elif order == "count,desc":
        sorted_inv = sorted(inv.items(), reverse=True,
                            key=lambda item: item[1])
    else:
        print("Wrong order. Choose again.")
        return

    if len(max(inv, key=len)) <= 9:
        length = 9
    else:
        length = len(max(inv, key=len))

    if len(str(max(inv.values()))) <= 5:
        val = 5
    else:
        val = len(str(max(inv.values())))

    print("Inventory:")
    print(" ", "count".rjust(val), " " * 2, "item name".rjust(length))
    print("-" * (6 + length + val))

    for item in sorted_inv:
        print (" ",
               str(item[1]).rjust(val),
               " " * 2, item[0].rjust(length))

    print("-" * (6 + length + val))
    print("Total number of items:", sum(inv.values()))


#Import/Export .csv file functions

def import_inventory(filename):

    import csv
    openfile = open(filename, encoding="utf-8")
    importlist = list(csv.reader(openfile))
    openfile.close()
    del(importlist[0])
    for item in importlist:
        item[0].strip(), (str(item[1])).strip()
        item[1] = int(item[1])
        if item[0] in inv.keys():
            inv[item[0]] += item[1]
        else:
            inv[item[0]] = item[1]


def export_inventory(filename):

    import csv
    openfile = open(filename, "a", newline="", encoding="utf-8")
    openfile.close()
    invlist = list(inv.items())
    exportfile = open(filename, "w", newline="", encoding="utf-8")
    writefile = csv.writer(exportfile)
    writefile.writerow(["item_name", "count"])
    for item in invlist:
        item[0].strip(), (str(item[1])).strip()
        writefile.writerow([str(item[0]), str(item[1])])
    exportfile.close()


#The program

display_inventory()

add_to_inventory(inv, dragon_loot)

print_table("count,desc")
print_table("count,asc")
print_table("item name,desc")
print_table()
print_table("xyz")

export_inventory("import_inventory.csv")
import_inventory("import_inventory.csv")
