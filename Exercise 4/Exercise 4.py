# Q.1:

a = int(input())

while a <= 0:
    a = int(input())

b = int(input())
while b <= 0:
    b = int(input())

if a != b:
    if a > b:
        while a != b:
            b = b - a
        print (a)
    elif b > a:
        while b != a:
            a = a - b
        print (b)
else:
    print (a)

# Q.2:

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print("Biggest number is", a)
elif b >= a and b >= c:
    print("Biggest number is", b)
else:
    print("Biggest number is", c)


# Q.3:

hours = int(input())
minutes = int(input())
seconds = int(input())

if seconds < 59:
    seconds += 1
else:
    seconds = 0
    if minutes < 59:
        minutes += 1
    else:
        minutes = 0
        if hours < 23:
            hours += 1
        else:
            hours = 0

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

# Q.4:

total_distance = 0

jump_distance = 1
for i in range(1000):
    total_distance += jump_distance
    jump_distance /= 2
    if total_distance == 2.5:
        print ("Yes")
        break
print ("No")

# Q.5:

price = float(input("Enter the base price: "))
operating_system = input("Enter the operating system: ")

if operating_system == "MacOS":
    price = price * 1.25
elif operating_system == "Linux":
    price = price * 0.8
elif operating_system != "Windows":
    price = price * 1.05

print("Final price:", price)



    

    

