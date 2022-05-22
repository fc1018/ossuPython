hrs = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hrs > 40 :
    pay = ((hrs - 40) * (rate * 1.5)) + (40 * rate)
else :
    pay = hrs * rate   
print("Pay:", pay)