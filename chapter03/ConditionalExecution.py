# try - except
rawstr = input('Enter a number')
try:
	ival = int(rawstr)
except:
	ival = -1

if ival > 0 :
	print('Nice work!')
else :
	print('Not a number')

astr = 'Bob'
try:
	print('Hello')
	istr = int(astr)
	print('There')
except:
	istr = -1
	
print('Done', istr)

astr = 'Hello Bob'
try:
	istr = int(astr)
except:
	istr = -1
	
print('First', istr)

astr = '123'
try:
	istr = int(astr)
except:
	istr = -1
	
print('Second', istr)

# Multi-way Puzzles
a = 6
if a < 2 :
	print('Below 2')
elif a < 20 :
	print('Below 20')
elif a < 10 :
    print('Below 10')
else :
	print('Something else...')

# If 
m = 11
if m < 2 :
	print('smaller')
elif m < 10 :
	print('Medium')
else :
	print('LARGE')
print('All done')

# If
x = 5
if x < 10:
	print('Smaller')
if x > 20:
	print('Biger')

print('Finis')
