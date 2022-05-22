def computepay(hrs, rate):
    if hrs > 40 :
        pay = ((hrs - 40) * (rate * 1.5)) + (40 * rate)
    else :
        pay = hrs * rate   
    return pay

try: 
    hrs = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
except:
    print("Error: Please enter numerical values ")
    quit()
    
earned = computepay(hrs, rate)
print("Pay", earned)