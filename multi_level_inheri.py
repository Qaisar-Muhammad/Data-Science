class Grandfather():
    def gfather(self):
        print("i am grandfather")

class Father(Grandfather):
    def sfather(self):
        print("i am father")
class son(Father):
    def sson(self):
        print("i am son ")

s=son()
s.gfather()
s.sfather()
s.sson()