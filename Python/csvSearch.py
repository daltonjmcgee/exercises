import re, csv, pyperclip

# print('What file do you want to open?')
# file = input()
#
# print('what domain are you looking for?')
# domain = input()

file = '/Users/dmcgee/Downloads/slack-verygreat-members.csv'

assemblybrands = re.compile(r'^.*@assemblybrands.com', re.VERBOSE)
verygreat = re.compile(r'^.*@verygreat.nyc', re.VERBOSE)
csv_file = csv.reader(open(file,'r'),delimiter=",")
newFile = open('/Users/dmcgee/Desktop/emails.txt','a+')

for row in csv_file:
    if assemblybrands.search(row[1]):
        newFile.write((row[1]) +  '\n')
    else:
        continue
newFile.close()
