# class student:
#     def student_details(self,name,age,salary,country):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.country=country

#     def shows_details(self):
#         print("your name is :",self.name)
#         print("your age is :",self.age)
#         print("your salary is :",self.salary)
#         print("your nationality is :",self.country)

# s1=student()
# s1.student_details("Qaisar muhammad",19,10000000,"pakistan")
# (s1.shows_details())



# class vehical:
#     def __init__(self,color,cast):
#         self.color=color
#         self.cast=cast

#     def show_detail(self):
#         print("color of vehical is:",self.color)
#         print("cast of vehical is :",self.cast)

# class car(vehical):  # here is used inheritance 
#     def show_car(self):
#         print("i am a car ")

# v2=vehical("Red",50000)
# v2.show_detail()

# c1=car("orange",1000)
# c1.show_detail()

# here is used override method 
class vehical:
    def __init__(self,color,cast):
        self.color=color
        self.cast=cast

    def show_detail(self):
        print("color of vehical is:",self.color)
        print("cast of vehical is :",self.cast)

class car(vehical):
    def __init__(self, color, cast,hp,seats):
        super().__init__(color, cast)
        self.hp=hp
        self.seats=seats
    def show_car(self):
        print("i am a car ")
        print("horse power of vehical is :",self.hp)
        print("seats are available in vehical are:",self.seats)

c1=car("orange",1000,89898,60)
c1.show_detail()
c1.show_car()