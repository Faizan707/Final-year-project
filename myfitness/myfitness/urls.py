from django.contrib import admin
from django.urls import path
from home.views import home, AddCustomer,Workout,customerlogin,customerDashboard,customerdiet,Addassistant,assistantmanagerlogin,assistantmanagerdashboard,CustomerFee,OtherAccounts
from contactUs.views import submit_message
from manager.views import managerlogin, manager_dashboard
from customer.views import create_customer, get_customer, delete_customer
from workout.views import workouts_list,customer_workouts_list
from diet.views import diet_create, diet_list, diet_delete
from assistant.views import create_assistant,get_assistant,delete_assistant
from accounts.views import create_customer_account,get_other_account,get_customer_account,create_other_account,delete_customer_account,delete_other_account
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
    path("customerfee/",CustomerFee,name="CustomerFee"),
    path("otheraccount/",OtherAccounts,name="OtherAccounts")
]
