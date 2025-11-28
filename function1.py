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