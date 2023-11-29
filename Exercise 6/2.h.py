n = int(input())
number = 1
for row in range (n + 1):
    # for column in range(row + 1):
        print (' ' * 2 * (n * 2 - row) + '  1 ' * (row + 1) + '' * 2 * (n * 2 - row))