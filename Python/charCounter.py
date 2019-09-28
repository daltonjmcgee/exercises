from pprint import pprint, pformat

message = 'If you import the pprint module into your programs, you’ll have access to the pprint() and pformat() functions that will “pretty print” a dictionary’s values. This is helpful when you want a cleaner display of the items in a dictionary than what print() provides. Modify the previous characterCount.py program and save it as prettyCharacterCount.py.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

print(f"Below is the count of each character in the following sentence: \n\n {message} \n\n {pformat(count)}")
