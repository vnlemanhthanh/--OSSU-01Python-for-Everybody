sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)
# print(fh,fr)
if fh > 40:
    # print('Overtime')
    reg = 40 * fr
    otp = (fh - 40) * (fr * 1.5)
    # print(reg, otp)
    xp = reg + otp
else:
    # print("Regular")
    xp = fh * fr

print(xp)