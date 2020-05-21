# WRITE A PROGRAM TO CHECK WHETHER INPUT NUMBER IS ODD/EVEN,PRIME,PALINDROME,ARMSTRONG.

num=int(input("enter the number you want to check : "))

# TO CHECK EVEN/ODD

a = num%2
if a == 0:
    print("even number")
if a != 0:
    print("odd number")

# TO CHECK PRIME

if num < 2:
    print("not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# TO CHECK PALINDROME NUMBER

rev = 0
a = num
while num > 0:
    digit = num % 10
    num = num // 10
    rev = rev * 10 + digit
if a == rev:
    print(a, "is a palindrome number")
else:
    print(a,"is not a palindrome number")


# TO CHECK ARMSTRONG NUMBER


sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit * digit * digit
    temp = temp // 10

if sum == temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not an armstrong number")

