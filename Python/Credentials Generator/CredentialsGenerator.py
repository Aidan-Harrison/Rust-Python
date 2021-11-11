# Credentials Generator
import random

class Person:
    firstName = ""
    surName = ""
    username = ""
    password = ""
    age = 1
    occupation = ""
    hobbies = ['']
    email = ""
    # Date of birth
    birthDay = 1
    birthMonth = 1
    birthYear = 1995

firstNames = [
    "Sarah",
    "John",
    "Richard",
    "Racheal",
    "Ripley",
    "Daniel",
    "Lucy"
]

surNames = [
    "Harrison",
    "Preston",
    "Jones",
    "Hunt"
]

occupations = [
    "Software Engineer",
    "Construction Worker",
    "Accountant",
    "Truck Driver",
    "Business Manager",
    "Unemployed"
]

hobbyList = [
    "Painting",
    "Programming",
    "Fishing",
    "Gardening",
    "Gaming",
    "Cooking"
]

def Login(person): # Login system
    credentials = ""
    print("Enter your username or email: ")
    input(credentials)
    while credentials != person.username or credentials != person.email:
        print("You have entered an invalid username or email!\nTry again:")
        input(credentials)
    print("Enter your password: ")
    input(credentials)
    while credentials != person.password:
        print("You have entered an invalid password\nTry again:")
        input(credentials)
    print("You have logged in!")


def CredentialsChecker(person):
    if len(username) < 6:
        print("Your username must contain at least 6 characters!")
        CreateAccount() # Check how scoping works in Python
    # Password checker, use map!??
    # email

def CreateAccount():
    customP = Person()
    print("Enter a username and password")
    input(customP.username)
    input(customP.password)
    print("Enter an email address")
    input(customP.email)

    CredentialsChecker(customP)

def PrintPerson(person, amount):
    print("(",amount + 1,")")
    print("Firstname: ", person.firstName)
    print("Surname: ", person.surName)
    print("Age: ", person.age)
    print("Date of birth:\n", person.birthDay, "/", person.birthMonth, "/", person.birthYear)
    print("Occupation: ", person.occupation)
    print("Hobbies: ", end='')
    for x in person.hobbies:
        print(x)
    print("E-Mail: ", person.email)
    print("=============================\n\n")

def CreatePerson(amount):
    index = 0
    for x in range(amount):
        p = Person()
        p.firstName = random.choice(firstNames)
        p.surName = random.choice(surNames)
        p.age = random.randrange(1, 100)
        if p.age > 18:
            p.occupation = random.choice(occupations)
        elif p.age > 65:
            p.occupation = "Retired"
        else:
            p.occupation = "Unemployed"
        # Date of Birth
        p.birthMonth = random.randrange(1,12)
        if p.birthMonth == 2:  # Do other months 
            p.birthDay = random.randrange(1,28)
        else:
            p.birthDay = random.randrange(1,31)
        p.birthYear = 2021 - p.age # Have current year based off PC date and time
        # Hobbies
        if p.age > 6:
            hobbyAmount = random.randrange(1,3)
            for x in range(hobbyAmount): # Prevent multiple of the same hobby from being added! Also prevent amount increasing based on amount of people generated
                p.hobbies.append(random.choice(hobbyList))

        # Create e-mail based off of person's name and/or date of birth
        p.email = p.firstName + p.surName + str(p.birthYear) + '@gmail.com'
        PrintPerson(p, x)

def Interface():
    print("What would you like to do:\n1) Generate  2)Create  3) Login")
    print("Set amount of people to generate: ")
    amount = input()
    while(int(amount) <= 0):
        print("Try Again!")
        amount = input()
    CreatePerson(int(amount))

Interface()
