# Q.1:

n = int(input())
fib0 = 0
fib1 = 1
counter = 2
while counter <= n:
    fib_next = fib0 + fib1
    fib0 = fib1
    fib1 = fib_next
    counter += 1
print (fib1)

# Q.2:

n = int(input())
x = float(input())
result = 1
term = 1
factorial = 1
counter = 1
while counter <= n:
    term = (term * x) / factorial
    result = result + term
    counter += 1
    factorial = factorial * counter
print (result)

# Q.3:
# Decreasing Loop:

n = int(input())
sum = 0
i = n
for x in range (i, 0, -1):
    sum = sum + x
print (sum)

# Base controlled loop:

n = int(input())
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i += 1
print (sum)

# Q.4:

s = input()
result = ''
index = 2
while index <= len(s) - 1:
    result += s[index]
    index = index + 3
print (result)