#Days in a month
def is_leap_year(year):
    if year%4==0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def day_in_month(year:int, month:int):
    try:
        month_days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
        num = 0
        if is_leap_year(year) and month == 1: 
            num = month_days_list[month] + 1
        else:
            num = month_days_list[month] 
    except Exception as e:
        print("Raise Exception index more than 11! Month should be 0 to 11",e)
    return num

print(day_in_month(2004, 1))


#Calculator

def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}




def recursive_calculate():
    num1 = float(input("What's the first number?\n"))    
    for symbols in operations:
        print(symbols)


    operation = input("Choose the above operation?\n")
    num2 = float(input("What's the next number?\n"))

    calculate_func = operations[operation]
    answer = calculate_func(num1,num2)
    print(answer)
    s =input("Do you want to continue? yes or no")
    flag = False
    while not flag:
        if s == "yes":
            flag = True
            num1=answer
            recursive_calculate()
        elif s == "no":
            flag = False

recursive_calculate()