# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s =0
c = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s = s+ float(line.strip().split(":")[-1])
    c = c+1
print("Average is",s/c)
