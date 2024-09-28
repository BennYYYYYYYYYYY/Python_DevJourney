# "Private"  means the attributes or methods are only available for the class members, not for the outsider of the class.
# add "__" at the front of the class name, then, that attribute or method will become private.

# Encapsulation: Traditionally, the OOP desigh emphasizes information hiding; this is known as "ensapsulation".(避免被直接改寫可能造成的錯誤) 
# 若真的需要使用到 private, 會 define public methods called "getter" and "setter". 
# [注意] 但在 Python, 這種方式非常不 Pythonic, 所以通常會用一個 "_" 表示他應該為 private 的概念。
# [注意] "We are all conseting adults." that means we trust each other, if someone want to make choas, they have to be responsible for their decision. 

class Robot:
    def __init__(self, name):
        self.name = name
        self.__age = 25 # private attribute(property)

    def __this_is_private(self): # private method
        print("hello from private method")

    def greet(self):
        print("Hi i'm a robot")
        self.__this_is_private()

    # setter (用來避免錯誤) -- not pythonic
    def age_setter(self, new_age):
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            print("New age setting is invalid")

    # getter (用來顯示 private 代表的值) -- not pythonic
    def age_getter(self):
        print(f"The age now is {self.__age}")


my_robot = Robot("Benny")
# my_robot.greet()
my_robot.age_setter(50)
my_robot.age_getter()



