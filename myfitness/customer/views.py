from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
import json

@csrf_exempt
def create_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        customer_id = data.get('customer_id')
        email = data.get('email')
        weight = data.get('weight')
        height_inches = data.get('height_inches')
        height_feet = data.get('height_feet')
        fitness_goal = data.get('fitness_goal')
        instructor_id = data.get('instructor_id')
        customer = Customer.objects.create(
            name=name,
            customer_id=customer_id,
            email=email,
            weight=weight,
            height_inches=height_inches,
            height_feet=height_feet,
            fitness_goal=fitness_goal,
            instructor_id=instructor_id
        )
        return JsonResponse({'message': 'Customer created successfully', 'id': customer.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_customer(request, customer_id):
    if request.method == 'GET':
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            data = {
                'name': customer.name,
                'customer_id': customer.customer_id,
                'email': customer.email,
                'weight': str(customer.weight),
                'height_inches': customer.height_inches,
                'height_feet': customer.height_feet,
                'fitness_goal': customer.fitness_goal,
                'instructor_id': customer.instructor_id
            }
            return JsonResponse(data)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_customer(request, customer_id):
    if request.method == 'DELETE':
        try:
            customer = Customer.objects.get(customer_id=customer_id)
            customer.delete()
            return JsonResponse({'message': 'Customer deleted successfully'})
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
