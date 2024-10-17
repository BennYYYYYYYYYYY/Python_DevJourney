'''
lambda expression:
Also known as "anonymous fuction", which means that we don't need to give it a name.

常跟 Higher oreder function 一起用，會自動 return。

The value computed by lambda expression will be returned automatically.
'''

# Lambda input1, input2, ...: operation

result = (lambda x: x ** 2)(5)  # 會自動 retrun
print(result) # 25


for item in map(lambda x: x ** 2, [15, 10, 5, 0]):
    print(item) # 225 100 25 0


for item in filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(item) # 0 2 4 6 8

