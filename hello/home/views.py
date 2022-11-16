from multiprocessing import context
from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        "variable":"variable is sent"
    }
    return render(request,'index_bs.html', context)
    #return HttpResponse("This is home page")

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')