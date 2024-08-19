'''
Higher Order function:
A function that take another function as a argument
'''

def higherOder(func):
    func()

def print_hello():
    print('Hello')

higherOder(print_hello) # Hello



# map function
def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]

for item in map(square, numbers):
    print(item) # 1 4 9 16 25 


# filter function  
def even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in filter(even, numbers):
    print(item) # 2 4 6 8 10 (Only for True) 




