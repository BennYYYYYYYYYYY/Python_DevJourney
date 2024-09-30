# For small programs, it's ok to pull all codes in a single .py file.
# However, if we put all codes together for large programs, it will be hard to write and maintain the codes.
# It would also be hard for a team to work together.

# Module: Divide codes into many different files.
# 1. Module are reusable.
# 2. We can have neat and shorter codes in each module.
# 3. Files are more orgizied.
# 4. Easier to maintain codes.


from myPackage.another_module import one_function # another_module (module) -> one_function (function)
from myPackage.sub_package import hello # hello -> module

one_function()  # 執行後會出現"__pycache__"資料夾，那是 python 自動把 module 的內容轉成 byte codes (電腦看的)，這樣 python 之後就能直接看 __pycache__ 內容，跑更快。
hello.small_hello()



# [題外話]  Module in python are objects
# 所以可以讓它使用 method, 也可以 print 出來

import random 
print(random.random()) 
print(random) # <module 'random' from 'C:\\User\\user\\anacoda3\\Lib\\random.py'>
