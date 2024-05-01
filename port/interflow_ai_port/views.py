from django.shortcuts import render

# Create your views here.
from django.shortcuts import render



def portfolio(request):
    return render(request, 'index.html')
