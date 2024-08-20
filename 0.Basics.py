# Copy by Value
int, float, str, tuple

# Copy by Reference
list, dict, set

# Tuple Unpacking
t = (1, 2, 3)
a, b, c = t

# Short-Circuit Evaluation
# 一旦整個表達式的結果可以確定，後續的部分就不再進行求值。
def test():
    print("Function called")
    return True

result = False and test() # "Function called" 不會被輸出，因為短路求值
result = True or test() # "Function called" 不會被輸出，因為短路求值


# Membership Operator
# in, not in
numbers = [1, 2, 3, 4, 5]
print(3 in numbers) # True
print(0 in numbers) # False
