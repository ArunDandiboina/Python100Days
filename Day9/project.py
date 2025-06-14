# Secret Bid.

import os

bids = {}
print("Welcome to the secret auction program.")
while True:
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    any_more_bids = input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    if any_more_bids == "no":
        # clear the console
        os.system('clear')
        break
    elif any_more_bids == "yes":
        # clear the console
        os.system('clear')
        continue

highest_bid = 0
highest_bidder = ""

for bidder, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")