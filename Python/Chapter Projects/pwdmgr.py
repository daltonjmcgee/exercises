#! /usr/bin/env python3

# pwdmgr.py is a password manager that will start out very insecure.

PASSWORDS = {
    '22189647334361':
        {'website':'https://gmail.com',
        'username':'dalton.mc@gmail.com',
        'password':'Jasperthedog!'}}

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

for k,v in PASSWORDS.items():
    if account in v['username']:
        pyperclip.copy(v['password'])
        print(f'Password for {account} copied to clipboard.')
    else:
        print(f'Couldn\'t find requested account.')
