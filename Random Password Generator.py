#Random Password Generator
import random
print("Generate your Random Password")
randomcharacters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTVWXYZ!@#$*_.?1234567890"
noofpassw=int(input("Enter the number of random passwords to be generate:"))
passwlength=int(input("Enter the length of the passwords you needed:"))
print("The Random PasswordS for You")
for i in range(noofpassw):
    pw=""
    for j in range(passwlength):
        pw=pw+random.choice(randomcharacters)
    print(pw)
print("Thank You :)")
