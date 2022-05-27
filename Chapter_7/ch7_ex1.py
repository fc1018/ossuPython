fileName = input("Enter a file name: ")
try:
    data = open(fileName)
except:
    print("Cannot open file ", fileName)
    quit()

for line in data:
    line = line.rstrip().upper()
    print(line)