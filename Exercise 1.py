# Assignments and Variables

# Task 1:

a = 8
b = 4
c = a + b
print (id(c))
print (type(c))
d = c
c = c / 3
print (id(c))
print (type(c))
print (id(d))
print (type(d))

# Task 2:

# Calculate the average age of students
student1 = 20
student2 = 25
student3 = 23
x = 19
s3 = 21
averageStudentAge = (x+(s3*(student1+student2)) + student3)/5
print(averageStudentAge)

# Mathematics:

# Task 1:

x = 0

xmin = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

x = 1.5
xmax = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

midpoint = (0.0 + 1.5) / 2

x = midpoint
xmid = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

next_midpoint = (0.0 + 0.75) / 2

x = next_midpoint
xmid = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

next_midpoint = next_midpoint / 2

x = next_midpoint
xmid = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

next_midpoint = next_midpoint / 2

x = next_midpoint
xmid = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

next_midpoint = next_midpoint / 2

x = next_midpoint
xmid = x ** 3 - 1.8 * x ** 2 - 1.2 * x + 1.6

print (xmid)

# Task 2:

import math
hyp = math.sqrt(41)
sine = 4/hyp
angle = math.asin(sine)
cos = math.cos(angle)
tan = sine / cos
calculated_tan = math.tan(angle)

print (tan, "vs", calculated_tan)

# Task 3:

print ("Input values:")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print (distance)

# Task 4:

print ("Input values:")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print (distance)

#  x1, y1, x2, y2, z need to be quadratic. z is the radius of the sector

arc = z * math.pi