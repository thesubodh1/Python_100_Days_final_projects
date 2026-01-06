bidders = {}

highest_bidder = ""
highest_bid = 0


more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid: $"))
    bidders[name] = bid
    more_bidders = input("Are there any more bidders? Type 'Yes' or 'No' ").lower()
    if more_bidders == "yes":
        more_bidders = True
        print("\n"*20)
    elif more_bidders == "no":
        more_bidders = False
    else:
        print("Please Type either yes or no!!!")
        more_bidders = False


for data in bidders:
    if bidders[data] > highest_bid:
        highest_bid = bidders[data]
        highest_bidder = data

print(f"The highest bidder was {highest_bidder} with the bid amount of ${highest_bid}")

