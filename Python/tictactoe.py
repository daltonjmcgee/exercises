theBoard = {'top——L': 'O', 'top——M': 'O', 'top——R': 'X',
            'mid——L': ' ', 'mid——M': 'X', 'mid——R': 'O',
            'low——L': 'X', 'low——M': ' ', 'low——R': ' '}
def printBoard(board):
    print(board['top——L'] + ' | ' + board['top——M'] + '| ' + board['top——R'])
    print('——+——+——')
    print(board['mid——L'] + ' | ' + board['mid——M'] + '| ' + board['mid——R'])
    print('——+——+——')
    print(board['low——L'] + ' | ' + board['low——M'] + '| ' + board['low——R'])
printBoard(theBoard)
