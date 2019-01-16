from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'blog/index.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def contact(request):
    if request.method ==  'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(emails=email_r,subject=subject_r,message=message_r)
        c.save()

        return render(request, 'blog/thanks.html')
    else:
        return render(request, 'blog/contact.html')