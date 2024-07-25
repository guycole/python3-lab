from decimal import Decimal
from typing import Dict

def rebalance(current_positions: Dict[str, Decimal],
              current_cash_usd: Decimal,
              current_prices_usd: Dict[str, Decimal],
              target_allocation: Dict[str, Decimal]) -> Dict[str, Decimal]:

    """
      Computes the quantities needed to rebalance a portfolio to the given target allocation.
    
      current_positions: map from ticker (AAPL) to quantity.
      current_cash_usd: free cash on the account.
      current_prices_usd: map from ticker to price. Can assume we have all valid prices for all relevant tickers.
      target_allocation: map from ticker to weight (for example 0.3). Must sum to 1. 
    
      return: the orders to buy or sell, map from ticker to quantity.
          If quantity is negative, it's a sell.
          If quantity is positive, it's a buy.
    
    """
    results = {}
 
    # find total value of account if sold
    # then find "balanced" value based on allocation
    # buy or sell shared to match that target

    # discover total value of account
    total_account_value = current_cash_usd
    for key, value in positions.items():
        position = current_positions[key]
        amount = current_prices_usd[key]
        result = position * amount
        total_account_value += result

    if total_account_value < 0:
        print("negative account value")
        return {}

    new_current_cash = 0
    for key, value in positions.items(): # AAPL
        allocation = target_allocation[key] # 0.3
        target_value = total_account_value * allocation
        target_pop = target_value / current_prices_usd[key]
        print(f"{key} {target_pop} {current_positions[key]}")
        if target_pop < current_positions[key]:
            fresh = current_positions[key] - target_pop
            print(f"buy {fresh} more {key}")
            results[key] = fresh 
        else:
            fresh = target_pop - current_positions[key]
            print(f"sell {fresh} of {key}")
            results[key] = -fresh 

    return results

positions = { 'AAPL': 100, 'GOOG': 200 }
current_cash = 123.0
current_prices = {'AAPL': 12.34, 'GOOG': 23.45}
allocations = {'AAPL': 0.3, 'GOOG': 0.7}

result = rebalance(positions, current_cash, current_prices, allocations)
print(result)
