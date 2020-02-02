from django.shortcuts import render

from .models import Job, Scan

def home(request):
    jobs = Job.objects
    #scan = Scan.btc_balance
    #btc_balance = Scan.btc_balance

    #test_object = "I'm a test object"

    hello = Scan.print_hello()
   

  
    return render(request,'jobs/home.html', {'jobs': jobs, 'hello': hello} )
    #return render(request, 'jobs/home.html', {'jobs':jobs, 'btc_balance':btc_balance, 'test_object':test_object})



