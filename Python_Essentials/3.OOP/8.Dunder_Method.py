# Dunder means "Double under(Underscores)" 
# They are commonly used for operator overloding. (定義 operator 在 class 用法) 

# beside __init__, __hash__, __eq__, the following list is some dunder methods can use in python.
# __len__: len()
# __str__: 常用在增加 user-readable string, str() or print()
# __repr__: 常用在 debug, stands for representation
# __add__: +
# __gt__: >
# __ge__: >=
# __it__: <
# __le__: <=

class Robot():
    def __init__(self, name, age, address):  # 定義初始狀態，設置 property
        self.name = name
        self.age = age 
        self.address = address

    # define a private method __key()
    def __key(self):
        return (self.name, self.age, self.address) 

    # implement hash function
    def __hash__(self):  # 定義 object 的 hash 值
        return hash(self.__key()) 
    
    def __eq__(self, other): # 定義 "==" 的方法
        if isinstance(other, Robot): 
            return self.__key() == other.__key()
        return NotImplemented 
    
    def __len__(self): # 定義 len()
        return self.age
    
    def __str__(self): # 定義 str(), 為了讀者的 readable
        return (f"{self.name} is now {self.age} years old, living in {self.address}")
    
    def __repr__(self): # 定義 repr(), 為了 debug
        return (f"name = {self.name}, age = {self.age}, address = {self.address}")

    def __add__(self, other): # 定義 "+"
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented
    
    def __gt__(self, other): # 定義 ">"
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented
    

