#! /usr/bin/env python

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\+?\d{1,3})?                  #country code
    (\s|-|\.)?                     #separator
    (\d{3}|\(\d{3}\))?             #area code
    (\s|-|\.)?                     #separator
    (\d{3})                        #first 3 digits
    (\s|-|\.)                      #separator
    (\d{4})                        #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       #At symbol
    [a-zA-Z0-9.-]+          #domain
    \.[a-zA-Z0-9]{2,4}      #upper level domain
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in emailRegex.findall(text):
    matches.append(groups)

for groups in phoneRegex.findall(text):
    if groups[1]:
        phoneNum = f"{groups[1]} "+'-'.join([groups[3], groups[5], groups[7]])
    else:
        phoneNum = '-'.join([groups[3], groups[5], groups[7]])
    if groups[8]:
        phoneNum+= f"Ext. {[groups[8]]}"
    matches.append(phoneNum)

if len(matches) > 0:
    MATCHES = '\n'.join(matches)
    pyperclip.copy(MATCHES)
    print("Copied to clipboard:")
    print(MATCHES)
else:
    print("No phone numbers or emails addresses")
