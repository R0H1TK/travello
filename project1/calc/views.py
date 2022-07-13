
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'one.html',{'name':'rohit'})
def home(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})
    # return HttpResponse(f"hi the value of {res} and the value of request is {request.GET['num1']}")

