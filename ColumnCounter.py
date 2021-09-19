# Column Counter

import sys
import numpy as np

filename = str(sys.argv[1])

file = open(filename, "r")

nums = []
counter = 0

# 6 max columns
columns = [[],[],[],[],[],[]]

for line in file:
    if line != ['\n','\r\n']:
        line = line.strip()
        linearr = line.split('-')
        linearr = np.array(linearr)
        linearr = linearr.astype(int)
        nums.append(linearr)

for i in nums:
    print(i)
    columns[0].extend(i[:1])
    columns[1].extend(i[1:2])
    columns[2].extend(i[2:3])
    columns[3].extend(i[3:4])
    columns[4].extend(i[4:5])
    columns[5].extend(i[5:6])

columncounter = 1;

for col in columns:
    unique, counts = np.unique(col, return_counts=True)
    print("Column " + str(columncounter) + ": ")
    ucounter = 0
    for u in unique:
        print(str(u) + " = " + str(counts[ucounter]))
        ucounter += 1
    columncounter += 1
    