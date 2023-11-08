# Q.1:

weights = [72, 5, 10, 2, 8, 14, 18, 20]

# Q.2:

weights.append(25)

# Q.3

for index in range (5, 1, -1):
    weights.remove(weights[index])

# Q.4:

weights.sort()
weights.reverse()

# Q.5:

weights.reverse()

# Q.6:

receivers = ['Bob', 'Doro', 'Prof Turtule', 'Asmee', 'Maria']

tuples = list(zip(receivers, weights))

# Q.7:

for item in tuples:
    if item[0] == 'Prof Turtule':
        print (item[1])

# Q.8:

# More efficient is using the dictionary

dictionary = {}
for item in tuples:
    dictionary[item[0]] = item[1]

# Q.9:

if 'Adam' in dictionary:
    print ('not shipped')
else:
    print ('shipped')

# Q.10:

new_list = []
for item in dictionary:
    if dictionary[item] < 10:
        new_list.append(dictionary[item] * 1000)

# Q.11:

work_done = (input('work done?'))

while work_done == 'no' or work_done == 'No':

    key = input()
    value = float(input())

    dictionary [key] = value

    work_done = (input('work done?'))

# Sort:

original_list = [1,4,7,3,2,8,6,9,5]

n = len(original_list)
     
for i in range(n):
    swapped = False

    for j in range(0, n-i-1):

        if original_list[j] > original_list[j+1]:
            original_list[j], original_list[j+1] = original_list[j+1], original_list[j]
            swapped = True
    if (swapped == False):
        break
 
print (original_list)

# Pythagoras Theorem:

pythagoras_list = []

combination = (3, 4, 5)
pythagoras_list.append(combination)

combination = (5, 12, 13)
pythagoras_list.append(combination)

combination = (7, 24, 25)
pythagoras_list.append(combination)

combination = (9, 40, 41)
pythagoras_list.append(combination)

combination = (11, 60, 61)
pythagoras_list.append(combination)

combination = (13, 84, 85)
pythagoras_list.append(combination)

# Using Loop:

looped_pythagoras_list = []

for c in range(1, 101):
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if a**2 + b**2 == c**2:
                looped_pythagoras_list.append((a, b, c))

print(looped_pythagoras_list)

    