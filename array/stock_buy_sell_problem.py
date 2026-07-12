def max_profit(array: list[int]):
    
    current_min_price = array[0]
    buy_price = array[0]
    
    max_profit = 0
    price_sold_at = 0
    
    
    for price in array[1:]:
        
        if price < current_min_price:
            current_min_price = price
        
        profit = price - current_min_price
        
        if profit > max_profit:
            max_profit = profit
            price_sold_at = price
            buy_price = current_min_price
            
    return max_profit, buy_price, price_sold_at


# Test case 01
test_prices = [7, 1, 5, 3, 6, 4]

print(max_profit(test_prices))