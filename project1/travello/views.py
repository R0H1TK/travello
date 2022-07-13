
from django.http import HttpResponse
from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    hello=destination.objects.all()
    return render(request,'index.html',{'d1': hello})
# def home(request):
#     val1=int(request.POST['num1'])
#     val2=int(request.POST['num2'])
#     res=val1+val2
#     return render(request,'result.html',{'result':res})
#     # return HttpResponse(f"hi the value of {res} and the value of request is {request.GET['num1']}")

