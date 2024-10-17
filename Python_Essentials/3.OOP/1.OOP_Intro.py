class Robot:  # The naming convention of class name is - always capitalize the first letter!
    # in classes, we can alse define docstring
    '''Robot class is for creating robot'''
    
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} is walking...')

    def sleep(self, hour):
        print(f'{self.name} is sleeping for {hour} hours...')


my_robot_1 = Robot('Benny', 25)
print(my_robot_1.__doc__) # see the docstring

my_robot_1.walk()
my_robot_1.sleep(15)





