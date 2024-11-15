n = int(input())
for row in range (n):
    asciiNumber = 64
    print ('   ' * (n - row), end ='')
    for column in range ((2 * row) + 1):
        print ('' * (n - row), end = '')
        if column < 0.5 * (2 * row) + 1:
            asciiNumber += 1
        else:
            asciiNumber -= 1
        character = chr(asciiNumber)
        print (' ', character, end = '')
    print ()