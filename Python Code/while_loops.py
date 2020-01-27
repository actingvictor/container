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

# homework
list5 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total5 = 0
i = 0

while i < len(list5):
    if list5[i] < 0:
        total5 += list5[i]
    i += 1
print(total5)

# answer
a_given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
atotal = 0

aj = len(a_given_list) - 1
while a_given_list[aj] < 0:
    atotal += a_given_list[aj]
    aj -= 1
print(atotal)

# len() function
list6 = ["hello", "goodbye", "see ya", "welcome"]

xy = len(list6)
print(xy)
