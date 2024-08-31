from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseServerError
from .models import ContactMessage

@csrf_exempt
def submit_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Saving the contact message to the database
        try:
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # Store the data in session
            request.session['contact_data'] = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
            }
            # Return success message
            return JsonResponse({'status': 'success', 'message': 'Message submitted successfully'})
        except Exception as e:
            # Return error message
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    elif request.method == 'GET':
        try:
            # Exclude the 'Chattat' entry from ContactMessage queryset
            contact_messages = ContactMessage.objects.exclude(subject='Chattat').order_by('-created_at')
            
            # Serialize queryset to JSON
            messages_data = [{'name': msg.name, 'email': msg.email, 'subject': msg.subject, 'message': msg.message, 'created_at': msg.created_at} for msg in contact_messages]
            
            return JsonResponse({'status': 'success', 'data': messages_data})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return HttpResponseServerError('Only GET and POST requests are allowed')
