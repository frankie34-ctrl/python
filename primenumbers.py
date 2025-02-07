try:
    num = int(input("Enter the number: "))
except ValueError:
    print("Please enter the Integer value!")
    exit()
isPrime = True
if num<2:
    isPrime = False
else:
    for i in range(2, num):
        if num%i == 0:
            isPrime = False
            break
if isPrime:
    print(num, "Number is Prime number.")
else:
    print(num, "Number is not a Prime number.")