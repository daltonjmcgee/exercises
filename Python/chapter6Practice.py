#1 /bin/usr/env Python3

'''
ASSIGNMENT:
Write a function named printTable() that takes a list of lists of
strings and displays it in a well-organized table with each column
right-justified. Assume that all the inner lists will contain the
same number of strings.

It also prints the table rotate 90° clockwise.
'''



tableData = [
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', '', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
            ]

def printTable(table):

    colWidths = [0] * len(table)

    for i in range(len(tableData[0])):
        for k in range(len(tableData)):
            length = len(tableData[k][i])
            column = colWidths[k]
            if length > column:
                colWidths[k] = length


    for i in range(len(tableData[0])):
        print('',end='\n')
        for j in range(len(tableData)):
            print((tableData[j][i].rjust(colWidths[j])),end=" ")

printTable(tableData)
