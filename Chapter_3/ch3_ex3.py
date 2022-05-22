score = float(input("Enter score: "))
if score > 1.0 or score < 0.0:
    print("Error score outside of valid range (0.0 - 1.0) ")
    quit()
elif score < 0.6:
    print("F")
elif score < 0.7:
    print("D")
elif score < 0.8:
    print("C")
elif score < 0.9:
    print("B")
else: 
    print("A")
