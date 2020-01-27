# Python 3.8
# Januart 26, 2020


# for loops
total = 0
for i in range(1, 5):
    total += i
print(total)

# while loops
total2 = 0
j = 1
while j < 6:
    total2 += j
    j += 1
print(total2)

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)

# introduction to break
given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for n in given_list2:
    if n <= 0:
        break
    total4 += n
print(total4)

# while break
# given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total5 = 0
i = 0
while True:
    total5 += given_list[i]
    i += 1
    if given_list[i] <= 0:
        break
print(total5)

# answer
list6 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
t = 0
i = 0
while i < len(list6):
    if list6[i] < 0:
        t += list6[i]
    i += 1
print(t)


# my shitty code
list5 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total5 = 0
i = 0

while list5[i] >= 0:
    i += 1
    if list5[i] < 0:
        break

while list5[i] < 0:
    i += 1
    total5 += list5[i]

print(total5)
