def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

try:
    terms = int(input("No. of terms: "))
    if terms > 0:
        fib(terms)
    else:
        print("Enter positive number.")
except:
    print("Invalid input.")
