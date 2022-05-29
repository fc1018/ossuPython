filename = input("Enter filename: ")
try:
    data = open(filename)
except:
    print("File can't be opened: ", filename)
    quit()

hourSent = dict()

for line in data:
    if "From " in line:
        word = line.split()
        hourSent[word[5][:2]] = hourSent.get(word[5][:2], 0) + 1
    else:
        continue

for hour,amount in sorted(hourSent.items()):
    print(hour, amount)