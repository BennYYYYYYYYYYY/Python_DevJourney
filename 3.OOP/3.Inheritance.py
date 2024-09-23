# Inheritance means inherit the attributes(property) and methods from the parent class
# The parent class
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f'{self.name} is sleeping.')

    def eat(self):
        print(f'{self.name} is eating food.')


# The child class 
class Student(People): # inherited from People
    def __init__(self, name, age, student_id):
      #  People.__init__(self, name, age) # People 換成 super(), 表superset, 他會 return 一個暫時的 object, 去取代原本的class 
        super().__init__(name, age) # 替換成 super()後不需要打 "self"
        self.student_id = student_id

    def eat(self, food):
        print(f'{self.name} is eating {food}.')


student1 = Student('Ben', 18, 15)
print(student1.name)
student1.eat("lamb")


