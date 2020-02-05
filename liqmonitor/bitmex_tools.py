# Import required modules

import requests
import pandas as pd
import numpy as np

import datetime as dt

import json
import pandas as pd
import numpy as np
import requests


class Orderbook():
    
    def __init__(self, symbol, depth):
        
        self.symbol = symbol
        self.depth = depth
        self.data = requests.get('https://www.bitmex.com/api/v1/orderBook/L2?symbol='+self.symbol+'&depth='+str(self.depth)).json()
        self.sells = [level for level in self.data if level.get('side') == 'Sell']
        self.buys = [level for level in self.data if level.get('side') == 'Buy']
        
    def show_best_buy_price(self):
        
        return self.buys[0].get('price')
    
    def show_best_sell_price(self):
        
        return self.sells[-1].get('price')
    
    def show_max_sell_size_for_slippage(self, slippage):
        
        best_sell_price = self.show_best_sell_price()
        max_sell_size = sum([level.get('size') for level in self.sells if level.get('price') < best_sell_price + (best_sell_price * slippage) ])
        return max_sell_size
    
    def show_max_buy_size_for_slippage(self, slippage):
        
        best_buy_price = self.show_best_buy_price()
        max_sell_size = sum([level.get('size') for level in self.buys if level.get('price') > best_buy_price - (best_buy_price * slippage) ])
        return max_sell_size

 
# Markets object for future development
 #class Markets_list():

    # def __init__(self):

      #  self.data = requests.get('https://www.bitmex.com/api/v1/instrument/active').json()

   # def show_markets(self):

     #   return self.data
