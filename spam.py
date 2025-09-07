fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(':')
        num = line[pos+1:]
        num = float(num)
        total = total + num
        count = count + 1
        continue

average = total / count

print("Average spam confidence:", average)
