# Python 3.8
# Januart 26, 2020


# defining a new function
import random


def function1():
    print("ahhh")
    print("ahhhh 2")


print("this is outside the function")


# recall the function1 below
function1()


# definining a function with 1 argument
def function2(x):
    return 2*x


# defining x as 3
a = function2(3)

# printing function2(3): 2 x 3
print(a)

# defining x as 4
b = function2(4)

# printing function2(4): 2 x 4
print(b)

# defining x as 5
c = function2(5)

# printing function2(4): 2 x 5
print(c)


# function with multiple arguments
def function3(x, y):
    return x + y


# defining x as 1, y as 2
e = function3(1, 2)

# printing variable e
print(e)

# new function


def function4(x):
    print(x)
    print("still in this function")
    return 3*x


f = function4(4)

print(f)


# new function
def function5(some_argument):
    print(some_argument)
    print("weeee")


function5(4)


# bmi calculator

# defining base variables
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's Sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's Brother"
height_m3 = 2.5
weight_kg3 = 160

# def [new function](argumet_1, argument_2, argument_3):


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)
print(" ")


# homework task converts miles into km
# km = 1.6 * miles

miles1 = 30
miles2 = 182
miles3 = 89


def convert(miles):
    conversionfunction = miles * 1.6
    print("Miles: ")
    print(conversionfunction)
    if conversionfunction > 0:
        return "successful"
    else:
        return "unsuccessful"


km1 = convert(miles1)
print(" ")
km2 = convert(miles2)
print(" ")
km3 = convert(miles3)
print(" ")

print(km1)
print(km2)
print(km3)

# random number generator

x = 0
while x < 10:
    print(random.randrange(1, 100))
    x += 1
