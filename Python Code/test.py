a = 1
b = 2
if a < b:
    print("a is less than b")
    print("possibility 1 has been successful")
print(" ")

c = 3
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is not less than d")
print("outside the IF block")
print(" ")

e = 19
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by ten")
else:
    print("e is greater than f")
print(" ")

g = 7
h = 6
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")
print(" ")

# defining base variables
name = "YK"
height_m = 2
weight_kg = 110

# defining secondary variables.
# secondary variables are variables that use other variables.
# as you can see in the example below we are using height_m (base variable)
# to define a new variable.
bmi = weight_kg / (height_m * height_m)

# using if else statements to dertimine somesones bmi.
print("bmi: ")
print(bmi)
if bmi < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
