from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'pages/customers.html')

def locations(request):
  return render(request, 'pages/locations.html')

def contacts(request):
  return render(request, 'pages/contacts.html')


