from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse('This is home page') 

def about(request):
    return render(request,'about.html') 

def post(request):
    return render(request,'post.html') 

def post2(request):
    return render(request,'post2.html') 

def post3(request):
    return render(request,'post3.html') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,
        date = datetime.today())
        contact.save()
        messages.success(request,'Message send successfully!')
    return render(request,'contact.html') 