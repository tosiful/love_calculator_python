print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combain_name=name1+name2
name_lower=combain_name.lower()

t=name_lower.count("t")
r=name_lower.count("r")
u=name_lower.count("u")
e=name_lower.count("e")

true=t+r+u+e

l=name_lower.count("l")
o=name_lower.count("o")
v=name_lower.count("v")
e=name_lower.count("e")

love=l+o+v+e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
  print(f"Your love_score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your love_score is {love_score}, you are alright together.")
else:
  print(f"Your love_score is {love_score}.")







