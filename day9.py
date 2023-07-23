from replit import clear
#travel log
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, num_of_visits, cities):
    print(travel_log)
    new_travel = {}
    new_travel["country"] = country
    new_travel["visits"] = num_of_visits
    new_travel["cities"] = cities
    travel_log.append(new_travel)

    print(travel_log)

add_new_country("Russia",3,["Moscow", "Saint Petersburg"])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4
print(dict)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])

#Secret Auction Program

print("Welcome to the Secret Auction!")

def add_bid(bid_list:list):
    name = input("Enter the name of the person!\n")
    amount = float(input(f"Enter the bid of the person {name}? $"))

    response = {
        "name": name,
        "bid": amount
    }
    bid_list.append(response)
    print(bid_list)
    return bid_list

def secret_auction(bid_list:list):
    continue_bid = input("Enter yes or no to continue bid!\n")
    if continue_bid == "yes":
        clear()
        bid_list = add_bid(bid_list)
        secret_auction(bid_list)
    elif continue_bid=="no":
        clear()
        winner_name = dict_max(bid_list)
        print(f"The winner of the bid is {winner_name}")

def dict_max(all_data:list):
    name = ""
    max_bid = 0
    for i in all_data:
        if i["bid"] > max_bid:
            max_bid = i["bid"]
            name = i["name"] 

    return name 

bid_list = []
bid_list = add_bid(bid_list)
secret_auction(bid_list)