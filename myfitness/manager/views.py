from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Manager
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def managerlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                manager = Manager.objects.get(name=name, password=password)
                return JsonResponse({'success': True})
            except Manager.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
        else:
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
