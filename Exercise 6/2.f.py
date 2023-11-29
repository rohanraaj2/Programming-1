n = int(input("Enter a number: "))
x = 1
count = 0
for row in range(1,n+1):
    for col in range(1,row+1):
        count += 1
        print(count, ' ', end="")
    print()
        