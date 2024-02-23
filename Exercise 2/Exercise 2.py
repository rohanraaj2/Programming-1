# Q.1:

# real: 3.13
# integer: -2

# Q.2:

# Q.i: True or False

# Q.ii:

a = True + False
print(a)

b = True + True
print(b)

c = False + False
print(c)

# Q.3:

a = -5
b = 3.2
c = True
d = 'st'

a = bool(a)
a = str(a)
# a = float(a)

b = int(b)
b = bool(b)
b = str(b)

c = str(c)
# c = float(c)
# c = int(c)

# d = float(d)
# d = int(d)
d = bool(d)

# Strings:

# Q.1:

notes = "Cucumber, Please remember to buuy the following things: \
Fish, Shell Polish, Fish, Slippers."
new_string = ''

for i in range(len(notes)):
    instance = notes[i - 1] == 'b' and notes[i + 1] == 'u'
    if instance == False:
        new_string += notes[i]
    
print (new_string)

# Q.2:

new_string = ''
word_list = notes.split()
count = 0
for word in word_list:
    if str(word) == 'Fish,':
        count += 1
    if count <= 1 or word != 'Fish,':
        if word[-1] == '.':
            new_string += word
        else:
            new_string += word + ' '

print (new_string)

# Q.3:

new_string = ''
for word in word_list:
    if str(word) != 'Cucumber,':
        if word == 'Slippers.':
            new_string += 'Slippers, '
        else:
            new_string += word + ' '
new_string += 'Cucumber.'

print (new_string)

# Q.4:

list_start = False
items = new_string.split()
line = 1
for word_number in range(len(items)):
    space = '   ' * line 
    if list_start == True:
        line += 1
        if items[word_number][-1] != ',' and items[word_number][-1] != '.':
            word = items[word_number] + " " + items[word_number + 1]
            word_number += 1
            print (space + word)
        else:
            print (space + items[word_number])
    if items[word_number] == 'Fish,' and list_start == False:
        list_start = True
        print (items[word_number])
    
# Q.5:

print(items)

# Q.6:

print (len(notes))
print ('The final length is', len(new_string))

# The length is the same
