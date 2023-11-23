# computepay funtion
def computepay(hours, rate):
    if hours > 40:
        reg = 40 * rate
        otp = (hours - 40) * (rate * 1.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay

# test client
sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
try:
    fh = float(sh)
    fr = float(sr)
except: 
    print("Invalid")
    quit()

pay = computepay(fh, fr)

print('Pay', pay)