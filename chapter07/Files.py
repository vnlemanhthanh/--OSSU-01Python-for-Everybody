
#
fh = open('mbox-short.txt')
print(len(fh.read()))

#
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count += 1
print('Line count: %d' %count)