from django.contrib import admin
from django.urls import path
from home.views import home, AddCustomer,Workout,customerlogin,customerDashboard,customerdiet,Addassistant,assistantmanagerlogin,assistantmanagerdashboard,CustomerFee,OtherAccounts,feeReport,dueFee,SalaryReports,ExpenseReports,ProfitReports,DailyReports,weeklyReports,YearlyReports,fitnessReport,backup,Customer_SignUp
from contactUs.views import submit_message
from manager.views import managerlogin, manager_dashboard
from customer.views import create_customer, get_customer, delete_customer
from workout.views import workouts_list,customer_workouts_list
from diet.views import diet_create, diet_list, diet_delete
from assistant.views import create_assistant,get_assistant,delete_assistant
from accounts.views import create_customer_account,get_other_account,get_customer_account,create_other_account,delete_customer_account,delete_other_account,update_customer_account,update_other_account
from reports.views import create_fee_report,get_fee_report,delete_fee_report,get_all_fee_reports,create_due_fee, get_all_due_fees, delete_due_fee,create_salary, get_all_salaries, delete_salary,create_expense, get_all_expenses, delete_expense,create_profit, get_all_profits, delete_profit,create_daily_report, get_all_daily_reports, delete_daily_report,create_weekly_report, get_all_weekly_reports, delete_weekly_report,create_yearly_report, get_all_yearly_reports, delete_yearly_report,create_fitness_report, get_all_fitness_reports, delete_fitness_report
from backup.views import create_backup
from customer_signup.views import customer_signup 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact-us/', submit_message, name="submit_message"),
    path("managerlogin/", managerlogin, name='managerlogin'),
    path("manager_dashboard/", manager_dashboard, name="manager_dashboard"),
    path('add-customer/', AddCustomer, name="AddCustomer"),
    path('create-customer/', create_customer, name='create_customer'),
    path('get-customer/<str:customer_id>/', get_customer, name='get_customer'),
    path('delete-customer/<str:customer_id>/', delete_customer, name='delete_customer'),
    path('workout/',Workout,name="Workout"),
    path('workouts/', workouts_list, name='workouts_list'),
    path('workouts/<str:customer_id>/', customer_workouts_list, name='customer_workouts_list'),
        path('customer/<str:customer_id>/update/', update_customer_account, name='update_customer_account'),

    path('customer-login/',customerlogin,name="customerlogin"),
    path("customer-dashboard/",customerDashboard,name="customerDashboard"),
    path('diet/create/', diet_create, name='diet_create'),
    path('diet/list/<int:customer_id>/', diet_list, name='diet_list'),
    path('diet/delete/<int:customer_id>/', diet_delete, name='diet_delete'),
    path('customerdiet/',customerdiet,name="customerdiets"),
    path('addassistant/',Addassistant,name="Addassistant"),
    path("create_assistant/",create_assistant,name="create_assistant"),
     path("get_assistant/<int:assistantID>/", get_assistant, name="get_assistant"),
    path("delete_assistant/<int:assistantID>/", delete_assistant, name="delete_assistant"),
    path("assistantlogin/",assistantmanagerlogin,name="assistantmanagerlogin"),
    path("assistantdashboard/",assistantmanagerdashboard,name="assistantmanagerdashboard"),
    path('customer/create/', create_customer_account,name="create_customer_account"),
    path('customer/<str:customer_id>/', get_customer_account,name="get_customer_account"),
    path('customer/<str:customer_id>/delete/', delete_customer_account,name="delete_customer_account"),
    path('other/create/', create_other_account,name="create_other_account"),
    path('other/<int:other_account_id>/', get_other_account,name="get_other_account"),
    path('other/<int:other_account_id>/delete/', delete_other_account,name="delete_other_account"),
        path('other/<int:other_account_id>/update/', update_other_account,name="update_other_account"),

    path("customerfee/",CustomerFee,name="CustomerFee"),
    path("otheraccount/",OtherAccounts,name="OtherAccounts"),
    path('fee_reports/', create_fee_report, name='create_fee_report'),
    path('fee_reports/<int:fee_report_id>/', get_fee_report, name='get_fee_report'),
    path('fee_reports/<int:fee_report_id>/delete/', delete_fee_report, name='delete_fee_report'),
    path('all_fee_reports/', get_all_fee_reports, name='get_all_fee_reports'),
     path('due_fees/', create_due_fee, name='create_due_fee'),
    path('due_fees/all/', get_all_due_fees, name='get_all_due_fees'),
    path('due_fees/<int:due_fee_id>/delete/', delete_due_fee, name='delete_due_fee'),
    path('salaries/', create_salary, name='create_salary'),
    path('salaries/all/', get_all_salaries, name='get_all_salaries'),
    path('salaries/<int:salary_id>/delete/', delete_salary, name='delete_salary'),
    path('expenses/', create_expense, name='create_expense'),
    path('expenses/all/', get_all_expenses, name='get_all_expenses'),
    path('expenses/<int:expense_id>/delete/', delete_expense, name='delete_expense'),
    path('profits/', create_profit, name='create_profit'),
    path('profits/all/', get_all_profits, name='get_all_profits'),
    path('profits/<int:profit_id>/delete/', delete_profit, name='delete_profit'),
   path('daily_reports/', create_daily_report, name='create_daily_report'),
    path('daily_reports/all/', get_all_daily_reports, name='get_all_daily_reports'),
    path('daily_reports/<int:daily_report_id>/delete/', delete_daily_report, name='delete_daily_report'),
    path('weekly_reports/', create_weekly_report, name='create_weekly_report'),
    path('weekly_reports/all/', get_all_weekly_reports, name='get_all_weekly_reports'),
    path('weekly_reports/<int:weekly_report_id>/delete/', delete_weekly_report, name='delete_weekly_report'),
    path('yearly_reports/', create_yearly_report, name='create_yearly_report'),
    path('yearly_reports/all/', get_all_yearly_reports, name='get_all_yearly_reports'),
    path('yearly_reports/<int:yearly_report_id>/delete/', delete_yearly_report, name='delete_yearly_report'),
    path('fitness_reports/', create_fitness_report, name='create_fitness_report'),
    path('fitness_reports/all/', get_all_fitness_reports, name='get_all_fitness_reports'),
    path('fitness_reports/<int:fitness_report_id>/delete/', delete_fitness_report, name='delete_fitness_report'),
    path('api/create_backup/', create_backup, name='create_backup'),

    path("feeReport/",feeReport,name="feeReport"),
    path("duefee/",dueFee,name="dueFee"),
    path("salaryReport/",SalaryReports,name="SalaryReport"),
    path("expense/",ExpenseReports,name="ExpenseReports"),
    path("profit/",ProfitReports,name="ProfitReports"),
    path("dailyreport/",DailyReports,name="DailyReports"),
    path("weeklyreport/",weeklyReports,name="weeklyReports"),
    path("yearlyreport/",YearlyReports,name="YearlyReports"),
    path("fitness-report/",fitnessReport,name="fitnessReport"),
    path("backup/", backup,name="backup"),
    path('customers/', customer_signup, name='customer_signup'),
    path('customer-signup/',Customer_SignUp,name="Customer_SignUp")

]
