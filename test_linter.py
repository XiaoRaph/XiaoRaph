import os # F401: os imported but unused

def my_func():
    print("hello") # E302: expected 2 blank lines, found 0
    unused_variable = 1 # F841: local variable 'unused_variable' is assigned to but never used

def another_func(): # E305: expected 2 blank lines after class or function definition, found 1
    pass
