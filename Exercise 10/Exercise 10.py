def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    
    fib0, fib1 = 0, 1
    counter = 2
    while counter <= n:
        fib_next = fib0 + fib1
        fib0, fib1 = fib1, fib_next
        counter += 1
    return fib1


def approximation(n, x):
    if n <= 0 or not isinstance(n, int):
        return "Invalid value of n. Please enter a positive integer."
    
    if not isinstance(x, (int, float)):
        return "Invalid value of x. Please enter a valid number."
    
    result = 1
    term = 1
    factorial = 1
    counter = 1
    while counter <= n:
        term = (term * x) / factorial
        result = result + term
        counter += 1
        factorial = factorial * counter
    return result


# Q.3:

def decreasing_loop(n):

    sum = 0
    i = n
    for x in range (i, 0, -1):
        sum = sum + x
    return sum

def base_controlled_loop(n):

    sum = 0
    i = 1

    while i <= n:
        sum = sum + i
        i += 1
    return sum

def third_letter_string(s):

    result = ''
    index = 2
    while index <= len(s) - 1:
        result += s[index]
        index = index + 3
    return result

def get_positive_integer():
    n = int(input())
    while n <= 0:
        print("Invalid value of n. Re-enter:")
        n = int(input())
    return n

n = input()

print("The result of the fibonacci series is:", fibonacci(n))

n = input()
x = float(input())

print("The approximate value of e is:", approximation(n, x))

n = input()

print ("Sum of numbers from 1 to n using a decreasing loop with step size -1 is", decreasing_loop(n)) 
print ("Sum of numbers from 1 to n using a base controlled loop is", base_controlled_loop(n))

s = input()

print("The final string is:", third_letter_string(s))

# Test cases for correct functionality
print("Test Case 1: Correct Functionality")
print("Fibonacci Series:")
print(f"Fibonacci(5): {fibonacci(5)}")  # Expected output: 5
print(f"Fibonacci(8): {fibonacci(8)}")  # Expected output: 21

print("\nApproximation:")
print(f"Approximation(5, 2): {approximation(5, 2)}")  # Expected output: 8.266666666666667
print(f"Approximation(7, 1.5): {approximation(7, 1.5)}")  # Expected output: 4.481481481481482

print("\nDecreasing Loop:")
print(f"Decreasing Loop Sum (10): {decreasing_loop(10)}")  # Expected output: 55
print(f"Decreasing Loop Sum (3): {decreasing_loop(3)}")  # Expected output: 6

print("\nBase Controlled Loop:")
print(f"Base Controlled Loop Sum (8): {base_controlled_loop(8)}")  # Expected output: 36
print(f"Base Controlled Loop Sum (4): {base_controlled_loop(4)}")  # Expected output: 10

print("\nThird Letter String:")
print(f"Third Letter String ('abcdefg'): {third_letter_string('abcdefg')}")  # Expected output: 'cf'

# Test cases for possible failures
print("\nTest Case 2: Possible Failures")
print("Fibonacci Series:")
print(f"Fibonacci(0): {fibonacci(0)}")  # Expected output: 0 (Edge case)

print("\nApproximation:")
print(f"Approximation(0, 2): {approximation(0, 2)}")  # Expected output: 1 (Edge case)
print(f"Approximation(3, -1): {approximation(3, -1)}")  # Expected output: 1 (Edge case)

print("\nDecreasing Loop:")
print(f"Decreasing Loop Sum (0): {decreasing_loop(0)}")  # Expected output: 0 (Edge case)

print("\nBase Controlled Loop:")
print(f"Base Controlled Loop Sum (0): {base_controlled_loop(0)}")  # Expected output: 0 (Edge case)

print("\nThird Letter String:")
print(f"Third Letter String ('ab'): {third_letter_string('ab')}")  # Expected output: 'b' (Edge case)
