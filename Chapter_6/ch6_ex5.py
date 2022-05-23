text = "X-DSPAM-Confidence:    0.8475"
numStart = text.find("0")
fExtractedValue = float(text[numStart:])
print(fExtractedValue)