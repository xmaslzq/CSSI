#factorial Calculator

a = int(raw_input("Key in the number that you want to factorial: "))
answer = 1;
for i in range(0,a):
    answer = answer * (i+1)
print(str(a) + "! = " + str(answer))
