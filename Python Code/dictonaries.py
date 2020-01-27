# Python 3.8
# Januart 27, 2020

# create dictionary
# d = dict() alternative
# d = {"key1": value1, "key2": value 2}

d = {}

# add entry to dictionary
d['George'] = 24
d['Tom'] = 32
d['Jenny'] = 16

# print value associated with key
print(d['George'])

# keys may only be certain data types
d[10] = 100
print(d)
print('')

# how to iterate over key-value pairs
for key, value in d.items():
    print('Key:')
    print(key)
    print('Value:')
    print(value)
    print('')
