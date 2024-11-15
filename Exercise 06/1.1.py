for term in range(1, 11):
    print (str(term ** 2), end = '')
    if term < 10:
        print (", ", end = '')
    else:
        print()