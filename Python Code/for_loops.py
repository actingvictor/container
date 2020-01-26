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
