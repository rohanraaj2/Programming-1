n = int(input())
for row in range (n):
    print (" " * 2 * (n - row - 1) + '* ' * (row + 1))