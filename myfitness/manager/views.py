from django.shortcuts import render, redirect
from .models import Manager

def managerlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            manager = Manager.objects.get(name=name, password=password)
            return redirect('manager_dashboard')  
        except Manager.DoesNotExist:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'manager.html', {'error_message': error_message})
    else:
        return render(request, 'manager.html')

def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')