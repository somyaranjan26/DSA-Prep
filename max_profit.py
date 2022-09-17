def find_max_profit(price):
    min_price = float('inf')     # Highly infinite number 
    max_profit = 0

    for i in range(len(price)):

        # finding min_price 
        if price[i] < min_price:
            min_price = price[i]

        # if it's not greater than min_price 
        # than we check if the differace of current price and min_price is greater or not.
        elif price[i] - min_price > max_profit:
            max_profit = price[i] - min_price
            
    return max_profit

price = [7,1,5,13,6,44]
print(find_max_profit(price))

#   Time Complexity: O(n)