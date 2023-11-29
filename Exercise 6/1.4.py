start = 10
for term in range(1, 11):
    if term > 5:
        result += 1
        print (result, end = '')
    else:
        result = start - term
        print (result, end = '')
    if term < 10:
        print (', ', end = '')
    else:
        print()