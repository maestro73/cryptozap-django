from django.db import models
from . import bitmex_tools

# Create your models here.

class Liquidity_scan(models.Model):

    def print_hello():

        return "hello there pirate"

   


class Bitmex(models.Model):

   

    def show_best_buy_price():

        orderbook = bitmex_tools.Orderbook('XBT', 0)

        orderbook_eth = bitmex_tools.Orderbook('ETH', 0)

        orderbook_ltc = bitmex_tools.Orderbook('LTC', 0)

        best_buy_price = orderbook.show_best_buy_price()

        best_buy_price_eth = orderbook_eth.show_best_buy_price()

        best_buy_price_ltc = orderbook.show_best_buy_price()

        return [best_buy_price, best_buy_price_eth, best_buy_price_ltc]


    def show_best_sell_price():

        orderbook = bitmex_tools.Orderbook('XBT', 0)

        orderbook_eth = bitmex_tools.Orderbook('ETH', 0)

        orderbook_ltc = bitmex_tools.Orderbook('LTC', 0)

        best_sell_price = orderbook.show_best_sell_price()

        best_sell_price_eth = orderbook_eth.show_best_sell_price()

        best_sell_price_ltc = orderbook.show_best_sell_price()


        return [best_sell_price, best_sell_price_eth, best_sell_price_ltc]


    def show_max_buy_size_for_slippage(slippage):

        orderbook = bitmex_tools.Orderbook('XBT', 0)

        orderbook_eth = bitmex_tools.Orderbook('ETH', 0)

        orderbook_ltc = bitmex_tools.Orderbook('LTC', 0)

        max_buy_size = orderbook.show_max_buy_size_for_slippage(slippage)

        max_buy_size_eth = orderbook_eth.show_max_buy_size_for_slippage(slippage)
        
        max_buy_size_ltc = orderbook_ltc.show_max_buy_size_for_slippage(slippage)

        return [max_buy_size, max_buy_size_eth, max_buy_size_ltc]


    def show_max_sell_size_for_slippage(slippage):

        orderbook = bitmex_tools.Orderbook('XBT', 0)

        orderbook_eth = bitmex_tools.Orderbook('ETH', 0)

        orderbook_ltc = bitmex_tools.Orderbook('LTC', 0)

        max_sell_size = orderbook.show_max_sell_size_for_slippage(slippage)

        max_sell_size_eth = orderbook_eth.show_max_sell_size_for_slippage(slippage)
        
        max_sell_size_ltc = orderbook_ltc.show_max_sell_size_for_slippage(slippage)


        return [max_sell_size, max_sell_size_eth, max_sell_size_ltc]

  


        






