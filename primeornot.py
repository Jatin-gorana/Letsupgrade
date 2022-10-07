# This program explains how to find a number is prime or not using python.

print("Enter a number to find if it is prime or not")

num = int(input())


def prime():
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


prime()
