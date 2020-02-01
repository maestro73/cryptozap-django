from django.db import models
from . import ftx

from . import liquidity_monitor
# Create your models here.

class Liquidity_scan(models.Model):

    def print_hello():

        return "hello there pirate"

    def print_balance():

        client = ftx.FtxClient()
        balance = client.get_balances()

        return balance

    def get_liquidity():

        liquidity = liquidity_monitor.get_liquidity(0.2)

        return liquidity
  
