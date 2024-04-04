from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Workouts
import json

@csrf_exempt
def workouts_list(request):
    if request.method == 'GET':
        workouts = Workouts.objects.all()
        data = [{'id': workout.id, 'customer_id': workout.customer_id, 'day': workout.day,
                 'workout_name': workout.workout_name, 'exercises': workout.exercises} for workout in workouts]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        # Handle POST request to create new workout
        try:
            data = json.loads(request.body)
            workout = Workouts.objects.create(customer_id=data['customer_id'], day=data['day'],
                                              workout_name=data['workout_name'], exercises=data['exercises'])
            return JsonResponse({'message': 'Workout created successfully', 'id': workout.id}, status=201)
        except KeyError:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

@csrf_exempt
def customer_workouts_list(request, customer_id):
    if request.method == 'GET':
        workouts = Workouts.objects.filter(customer_id=customer_id)
        data = [{'id': workout.id, 'customer_id': workout.customer_id, 'day': workout.day,
                 'workout_name': workout.workout_name, 'exercises': workout.exercises} for workout in workouts]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'DELETE':
        # Delete workouts associated with the specified customer ID
        workouts = Workouts.objects.filter(customer_id=customer_id)
        workouts.delete()
        return JsonResponse({'message': f'Workouts for customer ID {customer_id} deleted successfully'}, status=204)
