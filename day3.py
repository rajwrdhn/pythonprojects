#Odd Even

def oddEven(num):
    if type(num) == int:   
        if num % 2 == 0:
            print(f"Number {num} is even !")
        else:
            print(f"Number {num} is odd !")
    else:
        print(f"{num} is of type {type(num)} ! Please make sure the num is integer!")

oddEven(-26.3)
oddEven(26)


#BMI Calculator SI metrics unit

def bmicalculator(height, weight):
    bmi = round(weight / (height**2))

    if bmi < 18.5:
        print("The person is under weight!")
    elif 25 > bmi >= 18.5:
        print("The person is of Normal Weight!")
    elif 30 > bmi >= 25:
        print("The person is over weight!")
    else:
        print("The person is Obese!")


bmicalculator(1.75, 85)

#Leap year!

def leapyear(year):
    if type(year) == int and year > 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year!")
        elif year % 4 == 0 and year % 100 == 0:
            print(f"The year {year} is not a leap year!")
        elif year % 4 == 0:
            print(f"The year {year} is a leap year !")
        else:
            print(f"The year {year} is not a leap year !")
    else:
        print("Enter a positive integer value for year !")
leapyear(-2100)

#Pizza Order 

def pizzaorder():
    size = input("Enter the size of the pizza? L, M, S ! \n")
    pepperoni = input("Enter Y or N for pepperoni? \n")
    extra_cheese = input("Enter Y or N for extra cheese? \n")

    if size == "L":
        if pepperoni  == "Y" and extra_cheese == "Y":
            print("Your final bill is $", 29)
        elif pepperoni == "Y" and extra_cheese == "N":
            print("Your final bill is $", 28)
        elif pepperoni == "N" and extra_cheese == "Y":
            print("Your final bill is $", 26)
        else:
            print("Your final bill is $", 25)
    elif size == "M":
        if pepperoni  == "Y" and extra_cheese == "Y":
            print("Your final bill is $", 24)
        elif pepperoni == "Y" and extra_cheese == "N":
            print("Your final bill is $", 23)
        elif pepperoni == "N" and extra_cheese == "Y":
            print("Your final bill is $", 21)
        else:
            print("Your final bill is $", 20)
    else:
        if pepperoni  == "Y" and extra_cheese == "Y":
            print("Your final bill is $", 18)
        elif pepperoni == "Y" and extra_cheese == "N":
            print("Your final bill is $", 17)
        elif pepperoni == "N" and extra_cheese == "Y":
            print("Your final bill is $", 16)
        else:
            print("Your final bill is $", 15)


pizzaorder()

#Love Calculator

def lovecalculator():
    print("Welcome to the love calculator!")
    name1 = input("Enter the name of the first person? \n")
    name2 = input("Enter the name of the second person? \n")

    combined_name_lower = (name1 + name2).lower()

    t = combined_name_lower.count("t")
    r = combined_name_lower.count("r")
    u = combined_name_lower.count("u")
    e = combined_name_lower.count("e")
    true = t+r+u+e
    l = combined_name_lower.count("l")
    o = combined_name_lower.count("o")
    v = combined_name_lower.count("v")
    e = combined_name_lower.count("e")
    love = l+o+v+e
    truelove = int(str(true)+str(love))

    if truelove <10 and truelove > 90:
        print("Like coke and mentos!")
    elif truelove <50 and truelove > 40:
        print("You are alright together!")
    else:
        print(f"Your score is {truelove}.")

lovecalculator()
