from django.shortcuts import render

from .models import Liquidity_scan
from .models import Bitmex

# Create your views here.


def ftx(request):
    

    #hello = Liquidity_scan.print_hello()

    #liquidity = Liquidity_scan.get_liquidity()
    
  
    return render(request,'liqmonitor/ftx.html', {'hello': Liquidity_scan.print_hello(), 'balance':balance, 'liquidity': Liquidity_scan.get_liquidity()} )


def bitmex(request):


    best_buy_price = Bitmex.show_best_buy_price()

    best_sell_price = Bitmex.show_best_sell_price()

    if request.GET['slippage'] is '':
        slippage = 0.1
    else:
        slippage = float(request.GET['slippage'])
    



    liquidity_to_buy = Bitmex.show_max_buy_size_for_slippage(slippage)

    liquidity_to_sell = Bitmex.show_max_sell_size_for_slippage(slippage)

    btc_buy_liq = liquidity_to_buy[0]
    btc_sell_liq = liquidity_to_sell[0]
    eth_buy_liq = liquidity_to_buy[1]
    eth_sell_liq = liquidity_to_sell[1]
    ltc_buy_liq = liquidity_to_buy[2]
    ltc_sell_liq = liquidity_to_sell[2]

    return render(request, 'liqmonitor/bitmex.html', {
        'btc_buy_liq': btc_buy_liq, 
        'btc_sell_liq': btc_sell_liq,
        'best_buy': best_buy_price, 
        'best_sell': best_sell_price,
        'slippage': slippage,
        })

def hitbtc(request):

    return render(request, 'liqmonitor/hitbtc.html')