from django.shortcuts import render

from .models import Liquidity_scan

# Create your views here.


def home(request):
    

    #hello = Liquidity_scan.print_hello()

    #liquidity = Liquidity_scan.get_liquidity()
    
  
    return render(request,'liqmonitor/home.html', {'hello': Liquidity_scan.print_hello(), 'balance':balance, 'liquidity': Liquidity_scan.get_liquidity()} )
