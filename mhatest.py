# import inquirer
Name = input("What is your name? ")
yob = int(input("In which year were you born? "))
print("What is your gender? ")
response = None
while response not in {"Male", "Female"}:
    response = input("(Please Select Male or Female: ) e")
age = 2022 - yob
if age >= 50:
    if response == 'Male':
        print("Mallam "+Name+" Lalle an sha miya!")
    else:
        print("Malama " + Name + " Lalle an sha miya!")
else:
    if response == 'Male':
        print("Mallam "+Name+" yaya kuruciya?")
    else:
        print("Malama " + Name + " yaya kuruciya?")

