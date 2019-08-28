# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

# quarters
# nickels
# dimes
# pennies
# For each coin type, give yourself as many as you like.

# piggyBank = {
#     "pennies": 342,
#     "nickels": 9,
#     "dimes": 32
# }
# Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

# Given the coins shown above, the output would be 7.07 when you call calc_dollars()


def calc_dollars():
    piggy_bank = {
    "quarters": 500,
     "pennies": 100,
     "nickels": 400,
     "dimes": 100
    }

    quarter_amount = piggy_bank["quarters"] /4
    
    penny_amount = piggy_bank["pennies"] /100
    
    nickel_amount = piggy_bank["nickels"] /20
    
    dime_amount = piggy_bank["dimes"] /10
    

    total_amount = quarter_amount + nickel_amount + penny_amount + dime_amount
    
    print(total_amount)

calc_dollars()
