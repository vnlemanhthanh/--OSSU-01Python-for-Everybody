#
fname = input('Enter file name: ')
# fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened: %s' % fname)
    quit()

string = 'X-DSPAM-Confidence:'
count = 0
tot = 0

for line in fhand:
    if not line.startswith(string):
        continue
    # print(line)
    ipos = line.find(':')
    num = line[ipos+1:]
    num = float(num)
    count += 1
    tot += num

print('Average spam confidence:', tot/count)

