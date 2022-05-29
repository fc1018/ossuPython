import re

filename = input("Enter filename: ")
try:
    data = open(filename)
except:
    print("File can't be opened: ", filename)
    quit()

allNumbers = list()
total = 0

for line in data:
    numbers = re.findall("[0-9]+",line)
    for number in numbers:
        allNumbers.append(number)
    else:
        continue

for number in allNumbers:
    total += int(number)

print(total)