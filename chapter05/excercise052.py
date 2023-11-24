smallest = None
largest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None or num < smallest :
        smallest = num
    if largest is None or num > largest :
        largest = num
print('Maximum is %s' % largest)
print('Minimum is %s' % smallest)

    
