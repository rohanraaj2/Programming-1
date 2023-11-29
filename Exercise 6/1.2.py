result = 0
for term in range(1, 11):
    result += term
    print (str(result), end = '')
    if term < 10:
        print (", ", end = '')
    else:
        print()