filename = input("Enter filename: ")
try:
    data = open(filename)
except:
    print("File can't be opened: ", filename)
    quit()

count = 0
total = 0

for line in data:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    numStart = line.find("0")
    fExtractedValue = float(line[numStart:])
    total += fExtractedValue
    count += 1

print("Average spam confidence:", total/count)