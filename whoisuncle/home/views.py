from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage

def Home(request):
    return render(request,'home/home.html');
    # return HttpResponse('<h1>Hello World</h1>')

def Services(request):
    return render(request,'home/service.html');

def Contact(request):
    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        details = data.get('detail')
        print(title, email,details)
        
        
        if title == '' or email == '' :
            context['status'] = 'error'
            return render(request,'home/contact.html',context);
        
        new =ContactMessage()
        new.title = title
        new.email = email
        new.details = details
        new.save()
        context['status'] ='success'
        
        
    return render(request,'home/contact.html',context);