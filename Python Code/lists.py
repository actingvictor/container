# Python 3.8
# Januart 26, 2020

# defining a list
a = [3, 10, -1]
print(a)

# a.append will add to the list
a.append(1)
print(a)

a.append("hello")
print(a)

a.append([1, 2])
print(a)

# a.pop will remove the last entry from the list
a.pop()
print(a)

a.pop()
print(a)

# a[listnumber] will retrive an item from the list for the specified target
a[0]
print(a[0])

a[3]
print(a[3])

# a[0] = new item will replace an item from the list for the specified target
a[0] = 100
print(a)

# new list
b = ["bananna", "apple", "microsoft"]

temp = b[0]
b[0] = b[2]
b[2] = temp

print(b)
