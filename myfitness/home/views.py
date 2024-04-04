from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def AddCustomer(request):
    return render(request,'customer.html')

def Workout(request):
    return render(request,"workout.html")
def customerlogin(request):
    return render (request,"customerlogin.html")
def customerDashboard(request):
    return render (request,"customerDashboard.html")
def customerdiet(request):
    return render (request,"diet.html")