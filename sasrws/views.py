from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def loan(request):
    return render(request,"loan.html")

def trend(request):
    return render(request,"trend.html") 

def analytics(request):
    return render(request,"analytics.html")       

def checkup(request):
    return render(request,"checkup.html")
       
def base(request):
    return render(request,"base.html")       

def customers(request):
    return render(request,"customers.html")           