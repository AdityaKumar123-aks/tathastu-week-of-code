# PRINTING OF STAR PATTERN

n = int(input("enter the value of n :"))
for i in range(n):
    print("*" * (n-i) + "  " * i + "*" * (n-i))
for i in range(2,n+1):
    print("*" * i + "  " * (n-i) + "*" * i)
