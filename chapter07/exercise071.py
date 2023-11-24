
fname = 'mbox-short.txt'
fhand = open(fname)
# print(fhand)

for lx in fhand:
    ly = lx.rstrip()
    print(ly.upper())


