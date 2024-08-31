from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerAccounts, OtherAccounts
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def create_customer_account(request):
    if request.method == 'POST':
        data = request.POST
        try:
            customer = CustomerAccounts.objects.create(
                name=data['name'],
                customer_id=data['customer_id'],
                customer_fee=data['customer_fee'],
                status=data.get('status', 'unpaid')
            )
            return JsonResponse({'message': 'Customer account created successfully', 'id': customer.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def update_customer_account(request, customer_id):
    if request.method == 'POST':  # Using POST for update in this example
        data = request.POST
        try:
            customer = CustomerAccounts.objects.get(customer_id=customer_id)
            customer.name = data['name']
            customer.customer_fee = data['customer_fee']
            customer.status = data.get('status', customer.status)  # Update status if provided, else keep current
            customer.save()
            return JsonResponse({'message': 'Customer account updated successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Customer account not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def get_customer_account(request, customer_id):
    try:
        customer = CustomerAccounts.objects.get(customer_id=customer_id)
        return JsonResponse({
            'name': customer.name,
            'customer_id': customer.customer_id,
            'customer_fee': str(customer.customer_fee),
            'status': customer.status
        }, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Customer account not found'}, status=404)

@csrf_exempt
def delete_customer_account(request, customer_id):
    if request.method == 'DELETE':
        try:
            customer = CustomerAccounts.objects.get(customer_id=customer_id)
            customer.delete()
            return JsonResponse({'message': 'Customer account deleted successfully'}, status=204)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Customer account not found'}, status=404)

@csrf_exempt
def create_other_account(request):
    if request.method == 'POST':
        data = request.POST
        try:
            other_account = OtherAccounts.objects.create(
                rent_fee=data['rent_fee'],
                staff_fee=data['staff_fee'],
                status=data.get('status', 'unpaid')
            )
            return JsonResponse({'message': 'Other account created successfully', 'id': other_account.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def update_other_account(request, other_account_id):
    if request.method == 'POST':  # Using POST for update in this example
        data = request.POST

        try:
            other_account = OtherAccounts.objects.get(id=other_account_id)
            other_account.rent_fee = data['edit_rent_fee']
            other_account.staff_fee = data['edit_staff_fee']
            other_account.status = data['edit_status']
            other_account.save()
            return JsonResponse({'message': 'Other account updated successfully'}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Other account not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def get_other_account(request, other_account_id):
    try:
        other_account = OtherAccounts.objects.get(id=other_account_id)
        return JsonResponse({
            'rent_fee': str(other_account.rent_fee),
            'staff_fee': str(other_account.staff_fee),
            'status': other_account.status
        }, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Other account not found'}, status=404)

@csrf_exempt
def delete_other_account(request, other_account_id):
    if request.method == 'DELETE':
        try:
            other_account = OtherAccounts.objects.get(id=other_account_id)
            other_account.delete()
            return JsonResponse({'message': 'Other account deleted successfully'}, status=204)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Other account not found'}, status=404)
