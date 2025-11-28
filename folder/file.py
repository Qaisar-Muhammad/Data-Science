# print("hello dear")




# cart = []

# def add_item(item):
#     cart.append(item)
#     print(f"{item} added to cart.")

# def remove_item(item):
#     if item in cart:
#         cart.remove(item)
#         print(f"{item} removed from cart.")
#     else:
#         print(f"{item} is not in the cart.")

# def view_cart():
#     if cart:
#         print("Items in your cart:", ", ".join(cart))
#     else:
#         print("Your cart is empty.")



# # ---------------------------------

# add_item("Shirt")
# add_item("Shoes")
# view_cart()
# remove_item("Shirt")
# view_cart()

# a=[]
# def add(item):
#     a.append(item)
#     print(f"{a} is added to it")

# add(2999)











buying = []

def buyinglist(item, price):
    buying.append((item, price))
    print(f"Bought item: {item} it's price: {price}")

def count():
    total_items = len(buying)
    total_price = sum(price for item, price in buying)

    print(f"Total items: {total_items}")
    print(f"Total amount: {total_price}")

# Example usage
buyinglist("shoes", 3500)
buyinglist("shorts", 5000)
buyinglist("cotton cloth", 3000)
buyinglist("cloth battan", 600)
buyinglist("bata shoes",1900)
count()
