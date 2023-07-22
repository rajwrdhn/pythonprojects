import random
fruits = ["Apple","Banana", "Mango"]

for fruit in fruits:
    print(fruit)

#Average Height
def avg_height():
    heights = [175, 187, 183, 159, 165, 171]
    num = 0
    sum = 0 
    for height in heights:
        sum += height
        num +=1
    print(sum/num)
avg_height()

#Highest score in a list
def highest_score():
    scores = [90,91,94,88, 99,100, 92]

    highest = 0

    for i in scores:
        if i>highest:
            highest = i
    
    print(f"The highest score is {highest}.")

highest_score()

# Adding even numbers
def adding_even_nums():
    sum = 0
    for r in range(2,21,2):
        sum += r 

    print(sum)
adding_even_nums()

#FizzBuzz game
def fizzbuzz():
    for i in range(1,101,1):
        if i%3==0 and i%5==0:
            print("FIZZBUZZ")
        elif i%3==0:
            print("FIZZ")
        elif i%5==0:
            print("BUZZ")
        else:
            print(i)
            continue

fizzbuzz()

#PyPassword generator
def pass_generator():
    print("This is a pypassword generator!")
    num = int(input("Enter the length of the password!\n"))
    letters = ['a','b', 'c', 'A', 'B','C']
    symbols = ['$','_','-']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    letters.extend(symbols)
    letters.extend(numbers)
    pypass = []
    for n in range(0,num):
        random.shuffle(letters)
        pypass.append(letters[random.randint(0,18)])
    
    print(''.join(pypass))

pass_generator()
