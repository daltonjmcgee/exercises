from random import randint

alreadyAsked = False
response = ''

def askEightBall():
    global response
    global alreadyAsked

    messages = ['It is certain',
                'It is decidedly so',
                'Yes definitely',
                'Reply hazy try again',
                'Ask again later',
                'Concentrate and ask again',
                'My reply is no',
                'Outlook not so good',
                'Very doubtful']

    if alreadyAsked == False:
        while response != 'y' or 'n':
            print('Shake the 8-ball? (Y or N)')
            response = input().lower()
            if response == 'y' or 'n':
                break

    if response == 'y':
        print(messages[randint(0, len(messages) - 1)])
        print("Ask again? (Y or N)")
        answer = input().lower()
        if answer == 'y':
            alreadyAsked = True
            askEightBall()
    else:
        print('Okay. Talk later.')
    return


askEightBall()
