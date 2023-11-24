# Counting anh summing loops
count = 0
total = 0
largest = None
smallest = None
print('Before: largest(%s), smallest(%s)' % (largest, smallest))
for itervar in [3, 41, 12, 9, 74, 15]:
    count += 1
    total += itervar
    if largest is None or itervar > largest :
        largest = itervar
    if smallest is None or itervar < smallest :
        smallest = itervar
    print('Loop: %s %s %s %s %s' % (itervar, largest, smallest, count, total))
print('Largest:', largest)
print('Smallest:', smallest)
print('Count:', count)
print('Total:', total)
print('')

# Definite loops using for
friends = ['John', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: %s' % friend)
print('Done!')
print('')

# The while statement
while True:
    line = input('>>> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
print('')

#######
print('')
n = 5

while n > 0:
    print(n)
    n = n - 1

print('Blastoff')
print('')