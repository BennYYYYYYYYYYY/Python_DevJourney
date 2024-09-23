'''
Class Attributes: 屬於這個 "class" 的 attribute, 不放在 constructor 裡面(避免吃記憶體)
Class Method: 屬於這個 "class" 的 method, 不放在 constructor 裡面(避免吃記憶體), 可以用 cls 當作 first parameter (stands for class)

Class Attribute/Method 最好使用 self.__class__. 來呼叫, (不要直接打class的名是避免改class名稱後, 需要額外改code)
'''

class Circle:
    '''This class creates circle'''
    pi = 3.14159 # class attributes, not in constructor
    all_circles = [] # class methods, not in constructor

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self) # self.__class__. 呼叫

    def area(self):
        return self.__class__.pi * (self.radius ** 2)
    
    @classmethod
    def total_area(cls):  # "cls" as the parameter
        total = 0
        for circle in cls.all_circles: # classmethod version of self
            total += circle.area()
        return total
        

c1 = Circle(10)
c2 = Circle(15)

print(c1.area())
print(c1.__class__.total_area())
print(c2.__class__.total_area())



