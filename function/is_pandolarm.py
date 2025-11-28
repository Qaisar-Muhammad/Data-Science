#below code for pandolarm
# def is_pand(word):
#     reversed=word[::-1]
#     if word==reversed:
#         return True
#     return False
# print(is_pand("karak"))
# print(is_pand("qaisar"))


# below code for fibonicci series
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
num = int(input("Enter number of terms: "))
print("Fibonacci series:")
fibonacci_series(num)

