#
# Formatted String Literals
years = 3
count = .1
species = 'camels'
string = f'In {years} years I have spotted {count} {species}'
print(string)

# Parsing strings
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

# String methods
stuff = 'Hello, world'
print(type(stuff))
print(dir(stuff))

# String comparison
word = 'Pineapple'
word = word.lower()
if word < 'banana':
    print('Your word, ' + word + ', comes before banana')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana')
else:
    print('All right, banana')

# String are immutable
greeting  = 'Hello, world'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

# String slices
s = 'Monty Python'
print(s[0:5])

# Traversal through a string with loop
fruit = 'banana'
lenght = len(fruit)
index = 0
while index < lenght:
    letter = fruit[index]
    print(letter)
    index += 1
for char in fruit:
    print(char)
