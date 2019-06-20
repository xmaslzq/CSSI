# Say my Name
print("Project Name")
name = raw_input("Please enter your name: ") #
print("hola " + name);
print(" ")

# Guessing Game
print("Project Guess")
import random
secret = random.randint(0, 100)
r = 1
print(secret)
while r == 1:
    guess = int(raw_input("Guess the secret number: "))
    print(secret)
    if guess > secret:
        print("the number is smaller")
        r = 1
    if guess < secret:
        print("the number is bigger")
        r = 1
    if guess == secret:
        break
print("you guessed correctly!")
print(" ")

# Guess the number of seconds survived through knowing the age:
print("Project Age")
age = int(raw_input("Your Age: "))
leapTime = int( (age / 4) * (366 * 24 * 60 * 60) )
nonLeapTime = int( (age - age / 4) * (365 * 24 * 60 * 60) )
TotalTime = int(nonLeapTime + leapTime)
print("Total time survived: " + str(TotalTime))
print(" ")

#Find total result or average >= 60 pass < 60 fail
print("Project Result")
quiz = int(raw_input("Quiz result: "))
project = int(raw_input("porject result: "))
final = int(raw_input("finals result: "))
while quiz > 100 or project > 100 or final > 100:
    print("Stop lying! :( retype everything again")
    quiz = int(raw_input("Quiz result: "))
    project = int(raw_input("porject result: "))
    final = int(raw_input("finals result: "))

average = int((quiz + project + final) / 3)
if final < 60 or average < 60:
    print("You are not promoted")
else:
    print("You are promoted!")
print(" ")

#for loop
print("Project forloop")
msg = "hello Singapore"
h = 0
for char in msg:              #char
    if char == 'h':
        h = h + 1
print(str(h))

for idx in range(len(msg)):
    print(msg[idx])
#len_msg = len(msg)
#index_list = range(len_msg)
#for idx in index_list:
#    print(message[idx])
print(" ")

#encrypt message
#Task: Change the vowel in the msg (a,e,i,o,u)
print("Project Encrypt (failed)")
def cipher(code, mode, key):
    outp = ""
    new = ""
    for i in code:
        if mode == "en":
            new = chr(ord(i) + key)
            outp += new
        if mode == "de":
            new = chr(ord(i) - key)
            outp += new
    return("final" + mode + "code is " + str(outp))

code = raw_input("What do you want the code to be: ")
mode = raw_input("en (encode) or de (decode)? ")
key = int(raw_input("by how many alphabets? "))
print(cipher(code, mode, key))
print(" ")

#Rock Paper Scissors
