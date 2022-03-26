from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {'variable1':"EVERYTHING IS GREAT",
               'variable2':"NIKHIL IS GOOD",
               'variable3':"SHALOK IS GOOD"
    }
    messages.success(request, "this is a test message")
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')

    # return HttpResponse("this about page")

def services(request):
    return render(request, 'services.html')

    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your massages has been sent!')

    return render(request, 'contact.html')

    # return HttpResponse("this is contact page")