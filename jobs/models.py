from django.db import models
from . import ftx

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


class Scan(models.Model):

    
    


  

    def print_hello():

        return "hello there pirate"

    def show_balance():

        client = ftx.FtxClient()
        balances = client.get_balances()

        return balances[0].get('total')

    def get_current_btc_price():

        client = ftx.FtxClient()
        btc_price = client.get_orderbook('BTC-PERP')

        return btc_price

    #def get_websocket_ticker():

        #wsclient = ftx_websockets.FtxWebsocketClient()
        #ticker = wsclient.get_ticker('LTC-PERP')


