# Multiple Inheritance: inherit 多個 parent class.
# 不是所有的語言都可以用 Multiple Inheritance, 像 Java/Javascript 就不能用.
# Multiple Inheritance 看起來很複雜 readibility 很差, 所以其實盡量避免.

class E:
    pass

class F:
    def do_stuff(self):
        print("F do_stuff")

class G:
    def do_stuff(self):
        print("G do_stuff")

class B(E, F):
    pass

class C:
    def do_stuff(self):
        print("C do_stuff")

class D(G):
    pass

class A(B, C, D):
    pass

# A inherit了這麼多有do_stuff()的class後, 演算法在 do_stuff() 的呼叫到底會抓到誰的?
a1 = A()
a1.do_stuff() # "F do_stuff"

# 這個演算法的決定會依照 Python 的 MRO (Method Resolution Order) 去解決，而這邊使用的是 depth-first graph traversal algorithm.
# 可以利用 .mro() 或 .__mro__ 去查看 python 讀取 Calss 的順序
print(A.mro()) # return "list" 
print(A.__mro__) # return "tuple"
 
