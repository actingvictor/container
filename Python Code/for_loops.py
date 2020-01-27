# Python 3.8
# Januart 26, 2020

a = ["banana", "apple", "microsoft"]
for element in a:
    print(element)

b = [20, 10, 5]
total = 0
for all in b:
    print(all)
    total = total + all
    print(total)

# range function
c = list(range(1, 5))
print(c)

total2 = 0
for i in range(1, 5):
    total2 += i
    print(i)

print(list(range(1, 8)))

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)
print(" ")

# homework
total4 = 0
for i in range(1, 100):
    if i % 3 == 0:
        total4 += i

total5 = 0
for i in range(1, 100):
    if i % 5 == 0:
        total5 += i
gt = total4 + total5
print("total multiples of 3 & 5")
print(gt)
print(" ")

# homework ver 2
total6 = 0
for i in range(1, 100):
    if i % 3 == 0:
        print("multiple of 3: ")
        print(i)
        print(" ")

total7 = 0
for i in range(1, 100):
    if i % 5 == 0:
        print("multiple of 5: ")
        print(i)
        print(" ")
