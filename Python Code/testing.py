total4 = 0
for i in range(1, 100):
    if i % 3 == 0:
        total4 += i
print(total4)

total5 = 0
for i in range(1, 100):
    if i % 5 == 0:
        total5 += i
print(total5)

gt = total4 + total5

print(gt)
