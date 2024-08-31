from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ObjectDoesNotExist

from .models import FeeReport,DueFee,Salary,Expense,Profit,DailyReport,WeeklyReport,YearlyReport,CustomerFitnessReport

# Create (POST Request)
@csrf_exempt
def create_fee_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_name = data.get('customer_name')
        date = data.get('date')
        amount = data.get('amount')
        fee_report = FeeReport.objects.create(customer_name=customer_name, date=date, amount=amount)
        return JsonResponse({'id': fee_report.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Get (GET Request)
def get_fee_report(request, fee_report_id):
    if request.method == 'GET':
        try:
            fee_report = FeeReport.objects.get(id=fee_report_id)
            data = {
                'id': fee_report.id,
                'customer_name': fee_report.customer_name,
                'date': fee_report.date,
                'amount': fee_report.amount
            }
            return JsonResponse(data)
        except FeeReport.DoesNotExist:
            return JsonResponse({'error': 'FeeReport does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
def get_all_fee_reports(request):
    if request.method == 'GET':
        fee_reports = FeeReport.objects.all()
        data = [{'id': report.id, 'customer_name': report.customer_name, 'date': report.date, 'amount': report.amount} for report in fee_reports]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Delete (DELETE Request)
@csrf_exempt
def delete_fee_report(request, fee_report_id):
    if request.method == 'DELETE':
        try:
            fee_report = FeeReport.objects.get(id=fee_report_id)
            fee_report.delete()
            return JsonResponse({'message': 'FeeReport deleted successfully'})
        except FeeReport.DoesNotExist:
            return JsonResponse({'error': 'FeeReport does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

@csrf_exempt
def create_due_fee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_name = data.get('customer_name')
        amount_due = data.get('amount_due')
        status = data.get('status')
        due_fee = DueFee.objects.create(customer_name=customer_name, amount_due=amount_due, status=status)
        return JsonResponse({'id': due_fee.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

@csrf_exempt
def get_all_due_fees(request):
    if request.method == 'GET':
        try:
            due_fees = DueFee.objects.all()
            data = []
            for due_fee in due_fees:
                data.append({
                    'id': due_fee.id,
                    'customer_name': due_fee.customer_name,
                    'amount_due': due_fee.amount_due,
                    'status': due_fee.status
                })
            return JsonResponse(data, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'DueFee does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
# Delete (DELETE Request)
@csrf_exempt
def delete_due_fee(request, due_fee_id):
    if request.method == 'DELETE':
        try:
            due_fee = DueFee.objects.get(id=due_fee_id)
            due_fee.delete()
            return JsonResponse({'message': 'DueFee deleted successfully'})
        except DueFee.DoesNotExist:
            return JsonResponse({'error': 'DueFee does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

@csrf_exempt
def create_salary(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee_name = data.get('employee_name')
        amount = data.get('amount')
        date_paid = data.get('date_paid')
        salary = Salary.objects.create(employee_name=employee_name, amount=amount, date_paid=date_paid)
        return JsonResponse({'id': salary.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

def get_all_salaries(request):
    salaries = Salary.objects.all()
    data = []
    for salary in salaries:
        data.append({
            'id': salary.id,
            'employee_name': salary.employee_name,
            'amount': salary.amount,
            'date_paid': salary.date_paid.strftime('%Y-%m-%d')  # Convert date to string
        })
    return JsonResponse(data, safe=False)
# Delete (DELETE Request)
@csrf_exempt
def delete_salary(request, salary_id):
    if request.method == 'DELETE':
        try:
            salary = Salary.objects.get(id=salary_id)
            salary.delete()
            return JsonResponse({'message': 'Salary deleted successfully'})
        except Salary.DoesNotExist:
            return JsonResponse({'error': 'Salary does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
    
@csrf_exempt
def create_expense(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        category = data.get('category')
        amount = data.get('amount')
        date = data.get('date')
        expense = Expense.objects.create(category=category, amount=amount, date=date)
        return JsonResponse({'id': expense.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Get all expenses (GET Request)
def get_all_expenses(request):
    if request.method == 'GET':
        expenses = Expense.objects.all().values()
        return JsonResponse(list(expenses), safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Delete (DELETE Request)
@csrf_exempt
def delete_expense(request, expense_id):
    if request.method == 'DELETE':
        try:
            expense = Expense.objects.get(id=expense_id)
            expense.delete()
            return JsonResponse({'message': 'Expense deleted successfully'})
        except Expense.DoesNotExist:
            return JsonResponse({'error': 'Expense does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
@csrf_exempt
def create_profit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        income = data.get('income')
        expenses = data.get('expenses')
        totalprofit=data.get('totalprofit')
        profit = Profit.objects.create(date=date, income=income, expenses=expenses,totalprofit=totalprofit)
        return JsonResponse({'id': profit.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Get all profits (GET Request)
def get_all_profits(request):
    if request.method == 'GET':
        profits = Profit.objects.all().values()
        return JsonResponse(list(profits), safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Delete (DELETE Request)
@csrf_exempt
def delete_profit(request, profit_id):
    if request.method == 'DELETE':
        try:
            profit = Profit.objects.get(id=profit_id)
            profit.delete()
            return JsonResponse({'message': 'Profit deleted successfully'})
        except Profit.DoesNotExist:
            return JsonResponse({'error': 'Profit does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
@csrf_exempt
def create_daily_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        total_fees_collected = data.get('total_fees_collected')
        total_expenses = data.get('total_expenses')
        total_salary_paid = data.get('total_salary_paid')
        total_profit = data.get('totalprofit')  # Added total profit field
        daily_report = DailyReport.objects.create(date=date, total_fees_collected=total_fees_collected,
                                                   total_expenses=total_expenses, total_salary_paid=total_salary_paid,
                                                   totalprofit=total_profit)
        return JsonResponse({'id': daily_report.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Get all daily reports (GET Request)
def get_all_daily_reports(request):
    if request.method == 'GET':
        daily_reports = DailyReport.objects.all().values()
        return JsonResponse(list(daily_reports), safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Delete (DELETE Request)
@csrf_exempt
def delete_daily_report(request, daily_report_id):
    if request.method == 'DELETE':
        try:
            daily_report = DailyReport.objects.get(id=daily_report_id)
            daily_report.delete()
            return JsonResponse({'message': 'Daily report deleted successfully'})
        except DailyReport.DoesNotExist:
            return JsonResponse({'error': 'Daily report does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

@csrf_exempt
def create_weekly_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        total_fees_collected = data.get('total_fees_collected')
        total_expenses = data.get('total_expenses')
        total_salary_paid = data.get('total_salary_paid')
        total_profit = data.get('totalprofit')
        
        weekly_report = WeeklyReport.objects.create(
            start_date=start_date,
            end_date=end_date,
            total_fees_collected=total_fees_collected,
            total_expenses=total_expenses,
            total_salary_paid=total_salary_paid,
            totalprofit=total_profit
        )
        return JsonResponse({'id': weekly_report.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Get all weekly reports (GET Request)
def get_all_weekly_reports(request):
    if request.method == 'GET':
        weekly_reports = WeeklyReport.objects.all().values()
        return JsonResponse(list(weekly_reports), safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Delete (DELETE Request)
@csrf_exempt
def delete_weekly_report(request, weekly_report_id):
    if request.method == 'DELETE':
        try:
            weekly_report = WeeklyReport.objects.get(id=weekly_report_id)
            weekly_report.delete()
            return JsonResponse({'message': 'Weekly report deleted successfully'})
        except WeeklyReport.DoesNotExist:
            return JsonResponse({'error': 'Weekly report does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
@csrf_exempt
def create_yearly_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        year = data.get('year')
        total_fees_collected = data.get('total_fees_collected')
        total_expenses = data.get('total_expenses')
        total_salary_paid = data.get('total_salary_paid')
        total_profit = data.get('totalprofit')
        
        yearly_report = YearlyReport.objects.create(
            year=year,
            total_fees_collected=total_fees_collected,
            total_expenses=total_expenses,
            total_salary_paid=total_salary_paid,
            totalprofit=total_profit
        )
        return JsonResponse({'id': yearly_report.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Get all yearly reports (GET Request)
def get_all_yearly_reports(request):
    if request.method == 'GET':
        yearly_reports = YearlyReport.objects.all().values()
        return JsonResponse(list(yearly_reports), safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# Delete (DELETE Request)
@csrf_exempt
def delete_yearly_report(request, yearly_report_id):
    if request.method == 'DELETE':
        try:
            yearly_report = YearlyReport.objects.get(id=yearly_report_id)
            yearly_report.delete()
            return JsonResponse({'message': 'Yearly report deleted successfully'})
        except YearlyReport.DoesNotExist:
            return JsonResponse({'error': 'Yearly report does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
@csrf_exempt
def create_fitness_report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_name = data.get('customer_name')
        weight = data.get('weight')
        bodyfat = data.get('bodyfat')
        fitness_level = data.get('fitnessLevel')
        
        fitness_report = CustomerFitnessReport.objects.create(
            customer_name=customer_name,
            weight=weight,
            bodyfat=bodyfat,
            fitnessLevel=fitness_level
        )
        return JsonResponse({'id': fitness_report.id}, status=201)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

def get_all_fitness_reports(request):
    if request.method == 'GET':
        fitness_reports = CustomerFitnessReport.objects.all().values()
        return JsonResponse(list(fitness_reports), safe=False)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

@csrf_exempt
def delete_fitness_report(request, fitness_report_id):
    if request.method == 'DELETE':
        try:
            fitness_report = CustomerFitnessReport.objects.get(id=fitness_report_id)
            fitness_report.delete()
            return JsonResponse({'message': 'Fitness report deleted successfully'})
        except CustomerFitnessReport.DoesNotExist:
            return JsonResponse({'error': 'Fitness report does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
