from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def contact(request):
    return render(request, 'blog/contact.html')