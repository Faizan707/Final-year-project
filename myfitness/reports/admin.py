from django.contrib import admin
from .models import FeeReport, DueFee, Salary, Expense, Profit,DailyReport,WeeklyReport,YearlyReport,CustomerFitnessReport

admin.site.register(FeeReport)
admin.site.register(DueFee)
admin.site.register(Salary)
admin.site.register(Expense)
admin.site.register(Profit)
admin.site.register(DailyReport)
admin.site.register(WeeklyReport)
admin.site.register(YearlyReport)
admin.site.register(CustomerFitnessReport)