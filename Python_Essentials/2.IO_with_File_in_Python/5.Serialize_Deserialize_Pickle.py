# Serialization: process of converting an object into a format that can be easily stored or transmitted.
# Deserialization: the reverse process. It takes the serialized data and converts it back into the original object.

# Data ==(Serialization)==>  Medium(Binary) ==(Deserialization)==> Data

''' We need to make sure that the code we deserialize is not malicious '''

import pickle # python's module 

x = 0
y = 100
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def save_data(): # usually save the data as dictionary
    global x, y, my_list 
    data = {
        'x': x,
        'y': y,
        'my_list': my_list
    }

    with open('my_pickle_file', 'wb') as p_file: # write binary
        pickle.dump(data, p_file)

save_data()

def restore_data():
    global x, y, my_list
    with open('my_pickle_file', 'rb') as p_file: #  read binary
        data = pickle.load(p_file)
        x = data['x']
        y = data['y']
        my_list = data['my_list']

    print(x, y, my_list)

restore_data()

