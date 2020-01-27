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

# total multiples of 3 & 5 (wrong).
# multiples of 3 and 5 double up, such as 15.
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

# multiples of 3
total6 = 0
for i in range(1, 100):
    if i % 3 == 0:
        print("multiple of 3: ")
        print(i)
        print(" ")

# multiples of  5
total7 = 0
for i in range(1, 100):
    if i % 5 == 0:
        print("multiple of 5: ")
        print(i)
        print(" ")


# actual answer
atotal = 0
for i in range(1, 100):
    if i % 5 == 0:
        atotal += i
    elif i % 3 == 0:
        atotal += i
print(atotal)

# alternative answer
btotal = 0
for i in range(1, 100):
    if i % 5 == 0 or i % 3 == 0:
        btotal += i
print(btotal)

# more about for loops
# https://www.youtube.com/watch?v=iVyWLmQ0QYA&t=12s


# grab each element from a list variable
a = ["apple", "banana", "republic"]

for element in a:
    print(element)
print(" ")

# alternative grab
for i in range(len(a)):
    for j in range(i + 1):
        print(a[i])
print(" ")


# print custom range from a list
print("custom range: ")
for p in range(1, 3):
    print(a[p])
print(" ")

# actual answer
atotal = 0
for i in range(1, 100):
    if i % 3 == 0:
        atotal += i
    elif i % 5 == 0:
        atotal += i
print(atotal)
