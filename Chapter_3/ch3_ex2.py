try:
    hrs = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except: 
    print("Error, please enter numeric input ")
    quit()
    
if hrs > 40 :
    pay = ((hrs - 40) * (rate * 1.5)) + (40 * rate)
else :
    pay = hrs * rate   
print("Pay:", pay)