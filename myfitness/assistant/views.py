from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Assistant
import json
from django.utils.dateformat import format

@csrf_exempt
def create_assistant(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            assistant = Assistant.objects.create(
                assistantID=data.get("assistantID"),
                name=data.get("name"),
                phone_number=data.get('phone_number'),
                address=data.get('address'),
                qualification=data.get('qualification'),
                experience=data.get('experience'),
                available_from=data.get('available_from'),
                available_to=data.get('available_to')
            )
            return JsonResponse({'success': True, 'assistant_id': assistant.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
@csrf_exempt
def get_assistant(request, assistantID):
    if request.method == 'GET':
        try:
            assistant = Assistant.objects.get(id=assistantID)
            # Convert time to 12-hour format
            available_from_12h = format(assistant.available_from, 'h:i A')
            available_to_12h = format(assistant.available_to, 'h:i A')
            data = {
                'assistantID': assistant.id,
                'name': assistant.name,
                'phone_number': assistant.phone_number,
                'address': assistant.address,
                'qualification': assistant.qualification,
                'experience': assistant.experience,
                'available_from': available_from_12h,
                'available_to': available_to_12h
            }
            return JsonResponse(data)
        except Assistant.DoesNotExist:
            return JsonResponse({'error': 'Assistant not found'}, status=404)
@csrf_exempt
def delete_assistant(request, assistantID):
    if request.method == 'DELETE':
        try:
            assistant = Assistant.objects.get(id=assistantID)
            assistant.delete()
            return JsonResponse({'success': True})
        except Assistant.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Assistant not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
    