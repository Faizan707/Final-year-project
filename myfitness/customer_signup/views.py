from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerSignUp

@csrf_exempt
def customer_signup(request):
    if request.method == 'GET':
        customers = CustomerSignUp.objects.all()
        data = list(customers.values())
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        if name and password:
            customer = CustomerSignUp(name=name, password=password)
            customer.save()
            return JsonResponse({'message': 'Customer signed up successfully!'}, status=201)
        else:
            return JsonResponse({'error': 'Name and password are required.'}, status=400)
