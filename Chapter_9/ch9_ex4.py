filename = input("Enter filename: ")
try:
    data = open(filename)
except:
    print("File can't be opened: ", filename)
    quit()

emailsFrom = dict()

for line in data:
    if "From " in line:
        word = line.split()
        emailsFrom[word[1]] = emailsFrom.get(word[1], 0) + 1
    else:
        continue
# print(list(emailsFrom.items()))

maxSender = None
maxAmount = None
for sender,amount in emailsFrom.items():
    if maxSender is None or amount > maxAmount:
        maxSender = sender
        maxAmount = amount
        
print(maxSender, maxAmount)