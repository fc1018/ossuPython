filename = input("Enter filename: ")
try:
    data = open(filename)
except:
    print("File can't be opened: ", filename)
    quit()

total = 0

for line in data: 
    if "From:" not in line and "From" in line:
        word = line.split()
        print(word[1])
        total += 1
    else:
        continue
print("There were", total, "lines in the file with From as the first word")