from clear import clear 

from logo_auction import logo
# print(logo)

bids = {}
bidding_finished = False

def highest_bidder(bid_record):
    highest = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")

 
while not bidding_finished:
    print(logo)
    name = input("Please insert bidder name: ")
    price = int(input("Please insert price: "))
    bids[name] = price
    should_continue = input("Would you like to continue 'yes' or 'no' \n").lower()
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()
