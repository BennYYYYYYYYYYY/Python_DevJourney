x = [1, 2, 3]

# list comprehension
x_sqaured_list = [item ** 2 for item in x]

# dictionary comprehension
x_sqaured_dict = {item: item ** 2 for item in x}

# set comprehension
x_sqaured_set = {item ** 2 for item in x}

# generator comprehension (not tuple, cuz tuple is unmutable)
x_sqaured_generator = (item ** 2 for item in x) # generator object
print(x_sqaured_generator)  # memory address 
for i in x_sqaured_generator:
    print(i) # get what we want from generator





