from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'ICSapp/login.html')

def register(request):
    return render(request, 'ICSapp/register.html')

def statistic(request):
    return render(request, 'ICSapp/statistics.html')

def search(request):
    return render(request, 'ICSapp/search.html')

def home(request):
    return render(request, 'ICSapp/main.html')

def GetHtml(request,name):
    return render(request,'ICSapp/'+name)
