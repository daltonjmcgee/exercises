birthdays = {'brenna':'2/7/89', 'rob':"5/30/83", 'mom':'2/10/58'}

while True:
    print('Enter a name: (press Return to exit)')
    name = input().lower()
    if name == '':
        break

    if name in birthdays:
        print(name[0].upper() + name[1:] + "'s birthday is " + birthdays[name])
    else:
        print("I don't have that person in the birthday database")
        print("What is their birthday? (mm/dd/yy)")
        date = input()
        birthdays[name] = date
        print('Birthday database updated')
