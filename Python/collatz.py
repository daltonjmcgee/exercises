import sys

def collatz(number):
    if number % 2 == 0:
        val = round(number/2)
        print(val)
        return val
    else:
        val = round(3*number+1)
        print(val)
        return val
    

print('Choose a number')
try:
    choice = int(input())
except ValueError:
    print('you did not choose a number')
    sys.exit()

while choice != 1:
    print(choice)
    choice = collatz(choice)

if choice == 1:
    print('done!')
    sys.exit()
