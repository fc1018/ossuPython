def largesmall():
    largest = None
    smallest = None
    while True:
        val = input("Enter a value: ")
        if val == "done":
            break
        try:
            fval = int(val)
        except:
            print("Invalid input")
            continue
        if smallest == None:
            smallest = fval
        elif fval < smallest:
            smallest = fval
        elif largest == None:
            largest = fval
        elif fval > largest:
            largest = fval        
        else:
            continue
    print("Maximum is", largest)
    print("Minimum is", smallest)
largesmall()