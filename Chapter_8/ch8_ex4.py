filename = input("Enter filename: ")
try:
    data = open(filename)
except:
    print("File can't be opened: ", filename)
    quit()

lst = list()

for line in data:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort() # .sort() does not return a value
print(lst)