stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print(f"Inventory: ")
    item_total = 0
    for k,v in inventory.items():
        print(f"{str(v)} {k}" + ('s' if v > 1 else ''))
        item_total += v
    print(f"\nTotal number of items: {str(item_total)}\n")

displayInventory(stuff)

def addToInventory(inventory, itemsToAdd):
    item_total = 0
    for item in itemsToAdd:
        inventory.setdefault(item,0)
        inventory[item] += 1
        item_total += 1
        print(f"Added 1 {item}")
    print(f"\nTotal items added: {item_total} \n")

    displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(stuff,dragonLoot)
