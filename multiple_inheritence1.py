# class Father():
#     def work(self):
#         print("father is goint to work")

# class Mother():
#     def care(self):
#         print("mother is caring to all familt")

# class child(Father,Mother):
#     pass

# c=child()
# c.work()
# c.care()

# print(child.mro())


class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()

print(C.mro())
obj = C()

