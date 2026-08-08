import numpy as np

l = [10, 20, 30, 40, 50]

discount = 0.1
ld = []
for i in l:
    ld.append(i - (i*discount))

print(ld)