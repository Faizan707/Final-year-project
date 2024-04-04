from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Diet
import json

@csrf_exempt
def diet_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer_id = data.get('customer_id')
            break_fast = data.get('break_fast')
            lunch = data.get('lunch')
            preworkout = data.get('preworkout')
            postworkout = data.get('postworkout')
            dinner = data.get('dinner')

            diet = Diet.objects.create(
                customer_id=customer_id,
                break_fast=break_fast,
                lunch=lunch,
                preworkout=preworkout,
                postworkout=postworkout,
                dinner=dinner
            )
            return JsonResponse({'success': True, 'diet_id': diet.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def diet_list(request, customer_id):
    if request.method == 'GET':
        # Retrieve diets filtered by customer_id
        diets = Diet.objects.filter(customer_id=customer_id)
        # Convert queryset to JSON data
        data = [{'customer_id': diet.customer_id,
                 'break_fast': diet.break_fast,
                 'lunch': diet.lunch,
                 'preworkout': diet.preworkout,
                 'postworkout': diet.postworkout,
                 'dinner': diet.dinner} for diet in diets]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)


@csrf_exempt
def diet_delete(request, customer_id):
    if request.method == 'DELETE':
        try:
            diet = Diet.objects.get(customer_id=customer_id)
            diet.delete()
            return JsonResponse({'success': True})
        except Diet.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Diet not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
