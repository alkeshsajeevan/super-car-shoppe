from django.shortcuts import render
from .models import CarMake,CarModel

# from .models import 
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')


def cars(request):
    cars=CarModel.objects.all()
    return render (request,'myapp/cars.html',{'cars':cars})

def car_detail(request,id):
    cars=CarModel.objects.get(id=id)
    return render(request,'myapp/car_detail.html',{'cars':cars})

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def register(request):
    return render(request,'myapp/register.html')

def login(request):
    return render(request,'myapp/login.html')


def search(request):
    search=request.GET.get('search')
    cars=CarModel.objects.filter(brand__contains=search)
    return render (request,'myapp/search.html',{'cars':cars,'search':search})