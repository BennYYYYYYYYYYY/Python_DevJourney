with open('myfile.txt', mode = 'r', encoding='utf-8') as f:
    all_content = f.read() # return "string"
    print(all_content)

'''
mode:
    "r": 讀取(read)
    "w": 複寫(write)
    "a": 從最後一行開始新增(append)

'''

with open('myfile.txt', mode = 'a', encoding='utf-8') as f:
    f.write("New message\n")

    