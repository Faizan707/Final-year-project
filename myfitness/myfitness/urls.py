from django.contrib import admin
from django.urls import path
from home.views import home, AddCustomer,Workout,customerlogin,customerDashboard,customerdiet
from contactUs.views import submit_message
from manager.views import managerlogin, manager_dashboard
from customer.views import create_customer, get_customer, delete_customer
from workout.views import workouts_list,customer_workouts_list
from diet.views import diet_create, diet_list, diet_delete
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
    path('customerdiet/',customerdiet,name="customerdiets")
    
    
]
