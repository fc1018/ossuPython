from fileinput import filename


fileName = input("Enter a file name: ")
try:
    open(filename)
except:
    print("Cannot open file ", filename)
    quit()

for line in filename:
    line = line.rstrip().upper()
    print(line)