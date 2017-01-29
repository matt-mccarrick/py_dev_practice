#Given an array of inputs representing stock prices where the indices
#are the number of minutes past opening time and the values are the price in
#dollars of a given stock.

#Write an efficient function that takes stock_prices_yesterday and returns
#the best profit that can be made from one purchase and one sale of stock.

def get_max_profit(stock_prices_yesterday):
    if(len(stock_prices_yesterday) < 2):
        raise IndexError('Need at least two prices')

    #prime our loop to track our info greedily
    min_price = stock_prices_yesterday[0]
    max_profit_so_far = stock_prices_yesterday[1]-stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):
        #skip first because we already primed loop
        if(index==0):
            continue

        potential_profit = current_price - min_price
        max_profit_so_far = max(max_profit_so_far, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit_so_far
