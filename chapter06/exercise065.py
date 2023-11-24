#
text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
# print(ipos)
pieces = text[ipos+1:]
# print(pieces)
num = float(pieces)
print(num)