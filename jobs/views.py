from django.shortcuts import render

from .models import Job, Scan

def home(request):
    jobs = Job.objects
    #scan = Scan.btc_balance
    #btc_balance = Scan.btc_balance

    #test_object = "I'm a test object"

  
    return render(request,'jobs/home.html', {'jobs': jobs} )
    #return render(request, 'jobs/home.html', {'jobs':jobs, 'btc_balance':btc_balance, 'test_object':test_object})



