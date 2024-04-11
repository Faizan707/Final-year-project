import os
from django.http import JsonResponse, HttpResponse
from django.core.management import call_command
from django.views.decorators.csrf import csrf_exempt
from .models import BackupTask

@csrf_exempt
def create_backup(request):
    if request.method == 'POST':
        try:
            # Create BackupTask instance
            backup_task = BackupTask.objects.create(status='PENDING')
            # Trigger backup process
            call_command('dumpdata', output=f'backup_{backup_task.id}.json')
            backup_task.status = 'SUCCESS'
            backup_task.save()
            
            # Get the path to the backup file
            backup_file_path = os.path.join(os.getcwd(), f'backup_{backup_task.id}.json')
            
            # Open the backup file for reading
            with open(backup_file_path, 'rb') as backup_file:
                # Prepare the response with the file content for download
                response = HttpResponse(backup_file.read(), content_type='application/json')
                # Set the content-disposition header to trigger download
                response['Content-Disposition'] = f'attachment; filename=backup_{backup_task.id}.json'
                return response
        except Exception as e:
            backup_task.status = 'FAILED'
            backup_task.save()
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed for this endpoint.'}, status=405)
