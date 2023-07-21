import random 

def headstails():
    num = random.randint(0,1)

    if num == 0:
        print("Heads!")
    else:
        print("Tails!")

headstails()

states = ["Bihar", "Delhi", "TamilNadu", "Karnataka", "Meghalaya", "Nagaland"]

def raise_idex_err():
    try:
        print(states[6])
    except IndexError:
        print("List Index Error!")

raise_idex_err()

def banker_roullete():
    names = "Raj,Rohit,Pratik,Ali,Neel"
    list_names = names.split(",")

    rand_index = random.randint(0,len(list_names)-1)

    print(f"The payer is {list_names[rand_index]}")

banker_roullete()

def rock_paper_scissors():
    choice = "Rock, Paper, Scissors"
    list_choice = choice.split(",")

    human_choice = input("Enter Your choice ?  Rock , Paper or Scissors")
    comp_choice = list_choice[random.randint(0,2)]

    #More todo elif statements for other conditions
    if human_choice == list_choice[0] and comp_choice == list_choice[1]:
        print("Computer wins!")
    elif human_choice == list_choice[1] and comp_choice == list_choice[2]:
        print("Computer Wins!")
    elif human_choice == comp_choice:
        print("Draw !")

rock_paper_scissors()

