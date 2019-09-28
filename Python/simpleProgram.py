# this program asks for name and prints 'hello [name]'

print('Hello World')
print('What is your name?')
myName=input()
nameLength=len(myName)
print('Hey there ' + myName + '. Your name is ' + str(nameLength) + ' letters long.')
print('How old are you?')
myAge=input()
print("You'll be " + str(int(myAge)+1) + ' in a year.')
