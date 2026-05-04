n = int(input("Enter a number: "))

if n <= 1:
    print("it's not a Prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("it's not a Prime number")
            break
    else:
        print("it's a Prime number")
