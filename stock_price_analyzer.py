# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 17:22:38 2025

@author: henri
"""

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the max price and its day')
    print('(5) Find the min single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(list1):
    """returns the average price"""
    sum_price = 0
    for x in list1:
        sum_price += x
    return sum_price/len(list1)

def max_day(list1):
    """function that returns the index of the highest price"""
    max_price = list1[0]
    max_index = 0
    for i in range(len(list1)):
        if list1[i] > max_price:
            max_price = list1[i]
            max_index = i
    return max_index

def min_change_day(list1):
    """computes and returns the index of the later day with smallest adjacent change."""
    min_change = abs(list1[0]-list1[1])
    change_day = 1
    for i in range(len(list1)-1):
        change = abs(list1[i]-list1[i+1])
        if change < min_change:
            min_change = change
            change_day = i+1
    return change_day

def any_above(list1, n):
    """returns True if any price > n."""
    for x in list1:
        if x > n:
            return True
    return False

def find_tts(list1):
    """returns days to buy/sell for max profit; returns [buy, sell, profit]."""
    max_change = 0
    buy_day = 0
    sell_day = 0
    
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            change = list1[j] - list1[i]
            if change > max_change:
                max_change = change
                buy_day = i
                sell_day = j
    return [buy_day, sell_day, max_change]

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            max_price = max_day(prices)
            print('The max price is', prices[max_price], 'on day', max_price)
        elif choice == 5:
            min_change = min_change_day(prices)
            print('The min single-day change occurs on day', min_change)
            print('when the price goes from', prices[min_change - 1], 'to', prices[min_change])
        elif choice == 6:
            threshold = int(input('Enter your threshold: '))
            threshold_vals = any_above(prices, threshold)
            if threshold_vals == True:
                print('There is at least one price above', threshold)
            else:
                print('There are no prices above', threshold)
        elif choice == 7:
            invest = find_tts(prices)
            print(' Buy on day', invest[0], 'at price', prices[invest[0]])
            print('Sell on day', invest[1], 'at price', prices[invest[1]])
            print('Total profit:', invest[2])
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')