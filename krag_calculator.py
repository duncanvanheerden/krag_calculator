def krag_calc():

    price_in_rands = float(user_input)
    vat = price_in_rands / 1.15

    if price_in_rands > 0: 
        price_in_rands = vat * 0.43 
        print("Units:", round(price_in_rands, 2))
    if price_in_rands <= 0:
        print("Error, amount cannot be < or = 0.0")
    return price_in_rands

user_input = input("Enter the amount you wish to purchase: R ")
krag_calc()    
