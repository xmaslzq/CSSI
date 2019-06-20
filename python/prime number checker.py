print("""Prime Number Checker 2.0
         created for simple use
      """)

check_prime = raw_input("What number do you want to check? ")
true = 0
nth = 0
if int(check_prime) > 1:
    for num in range(2, int(check_prime)) :
        if (int(check_prime) % num == 0 ):
            true = 0
            break
        else:
            true = 1
if (true == 1):
    print(check_prime + " is a prime number")
    for num in range(2, int(check_prime) + 1):
        for n in range(2, int(check_prime) + 1):
            if (num % n == 0):
                if (num != n):
                    break
                if (num == n):
                    nth = nth + 1
                    print(str(n))
    print("In fact, it is the " + str(nth) + "th prime number")
if (true == 0):
    print(check_prime + " is not a prime number")
