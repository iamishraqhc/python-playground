from contextlib import ContextDecorator
from typing import ContextManager

# structural pattern matching

def http_success(status):
    match status:
        case 200:
            print("OK")
        case 201:
            print("Created") 
        case 202:
            print("Accepted")
        case _:
            print("Error")
        
code = int(input())
http_success(code)

# Parenthesized Context Managers

with (
    ContextManager as ctx1,
    ContextDecorator as ctx2
):
    pass

# strict argument for zip function

names = ['Harry', 'Peter', 'Mark']
ages = [28, 24]

result1 = zip(names, ages)
print(list(result1)) # [('Harry', 28), ('Peter', 24)]

result2 = zip(names, ages, strict=True)
print(list(result2)) # ValueError: zip() argument 2 is shorter than argument 1

# Improved Error Messages

print("Hello") # SyntaxError: '(' was never closed
