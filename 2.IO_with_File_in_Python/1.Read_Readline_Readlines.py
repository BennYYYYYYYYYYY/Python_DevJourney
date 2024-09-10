file = open('myfile.txt') # return a file object

print(file.read()) # method to file object, return "string"
file.seek(0) # let "seek" back to the first line
print(file.read(2), file.read(5)) # Hi / , how 


print(file.readlines()) # return a "list" of lines. (可能會幹爆RAM)


print(file.readline()) # 每次讀取一行，return "string", base on seek (更好節省RAM的方式)
while True:
    line = file.readline()
    if not line: # []=False, not False = True , 若有string = True, 經過 not = False 
        break
    else:
        print(line)


file.close() # save RAM


