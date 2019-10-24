import re, pyperclip, requests, os

url = re.compile(r'''(
    https?:\/\/                          #http/https
    (www\.)?                             #www subdomain
    [-a-zA-Z0-9@:%._\+~#=]{1,256}\.      #domain
    [a-zA-Z0-9()]{1,6}                   #top-level domain
    \b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)    #directory
    )''', re.VERBOSE)

text = str(pyperclip.paste())
numberOfFiles = 0

print('Which folder do you want to save to?')
print('Tip: navigate to folder in Terminal and use pwd command.')
folder =  input()


for groups in url.findall(text):
    req = requests.get(groups[0])
    if req.status_code == 200:
        dir = groups[2].split("/")
        filename = dir[len(dir)-1]
        file = open(f"{folder}/{filename}", 'wb')
        file.write(req.content)
        file.close()
        numberOfFiles += 1
        print(f"File {filename} downloaded")

print(f"{numberOfFiles} total files downloaded")
