# Shelve module can be used as a simple persistent storage for python objects
# Shelve module provides a simple interface that behaves like a dictionary. 
# You can store key-value pairs, where the key is typically a string and the value can be any picklable Python object.


import shelve

integers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
integers2 = [999, 998, 997, 996]
integers3 = [100, 101, 102, 103, 104, 105, 106, 107]

# save data
with shelve.open('my_shelve', 'c') as db: # "c" create
    db['ints1'] = integers1
    db['ints2'] = integers2
    db['ints3'] = integers3


# restore data
with shelve.open('my_shelve', 'r') as db: # "r" read
    for key in db.keys(): # shelve is like a dictionary
        print(key) # print every key

    print(db['ints2'])



