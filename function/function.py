# def add(a,b):
#     return a + b
# sum=add(45,88)
# print(sum)
# c=int(input("enter a number:"))
# d=int(input("enter a number:"))
# su=add(c,d)
# print("the sum of two number :",su)


# def char(name):
#     return name[0:4]
# print(char("qaisar"))

# def oddeeven(num):
#     if num%2 == 0:
#         return("even")
#     else:
#         return("odd")
    
# print(oddeeven(67))  
# print(oddeeven(670)) 


# def oddeeven(num):
#     if num%2 == 0:
#         return("even")
#     return("odd")
    
# print(oddeeven(67))  
# print(oddeeven(670)) 

# def oddeeven(num):# this method return
#     return num%2 == 0
    
# print(oddeeven(67))  
# print(oddeeven(670)) 

# def song():
#     return "laila song"
# print(song())

# def grater(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num1=int(input("enter a frist number:"))
# num2=int(input("enter a second number:"))
# biger=grater(num1,num2)
# print(f"{biger} is greater")

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# print(greatest(4588,77,666))   

# def new_greatest(a,b,c):
#     biger=grater(a,b)
#     return grater(biger,c)

# print(new_greatest(3434,656,785))

# Initial account data
# account_owner = "Atif Khan"
# account_balance = 500

# def check_balance():
#     print(f"Account balance: ${account_balance}")

# def deposit(amount):
#     global account_balance
#     account_balance += amount
#     print(f"${amount} deposited. New balance: ${account_balance}")

# def withdraw(amount):
#     global account_balance
#     if amount <= account_balance:
#         account_balance -= amount
#         print(f"${amount} withdrawn. New balance: ${account_balance}")
#     else:
#         print(f"Insufficient funds! Current balance: ${account_balance}")

# (deposit(100))0
# (withdraw(700))



# amount=int(input("enter a amount number :"))
# def pak_to_dollar(amount):
#     return amount/278
# def dollar_to_pak(dollor):
#     return dollor*278
# print(pak_to_dollar(1000))
# print(dollar_to_pak(1000))

# for rum time 
def rupees_to_dollor(rupees):
    a=rupees*278
    print(f"pakistani pkr {rupees} in dollor is equal to :{a}  ")

def rupees_in_dollor(dollor):
    b=dollor/278
    print(f"dollor $ {dollor} in pkr is equal to :{b}  ")

rupees=int(input("enter a amount in rupees:"))
dollor=int(input("enter a amount in dollor :"))
rupees_to_dollor(rupees)
rupees_in_dollor(dollor)
     