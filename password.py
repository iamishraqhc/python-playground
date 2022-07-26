import random

alpha_small = 'abcdefghijklmnopqrstuvwxyz'
alpha_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!@#$%^&*_-+='

characters = alpha_small + alpha_cap + numbers + symbols

length = 16
password = "".join(random.sample(characters, length))
print('Generated password: ', password)
