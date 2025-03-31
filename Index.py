#calculate_discount(price, discount_percent)
price = float(input("Enter the price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Variable
    # new_price
    
    if discount_percent >= 20:
        discount_percent = discount_percent / 20
        discount = discount_percent * price
        new_price = price - discount
        print("The new price is: ", new_price)
    elif discount_percent < 20:
        print("The new price is too low ")
    elif discount_percent > 20:
        print("The new price is too high")
    else:
        print("Invalid input")
