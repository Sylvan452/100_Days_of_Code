print("Welcome to the Love Calculator!")
myName = input("What is your name? \n").lower()
herName = input("What is their name? \n").lower()

combined_name = myName + herName

# Counting the number of times each letter occurs in the combined name
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e

lovescore = int(str(true) + str(love))

if lovescore < 10 or lovescore > 90:
    print(f"Your love score is {lovescore}, you go together like coke and mentos.")
elif lovescore >= 40 and lovescore <= 50:
    print(f"Your love score is {lovescore}, you are alright together.")
else:
    print(f"Your love score is {lovescore}.")
