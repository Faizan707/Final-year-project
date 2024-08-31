from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def AddCustomer(request):
    return render(request,'customer.html')

def Workout(request):
    return render(request,"workout.html")
def customerlogin(request):
    return render (request,"customerlogin.html")
def customerDashboard(request):
    return render (request,"customerDashboard.html")
def customerdiet(request):
    return render (request,"diet.html")
def Addassistant(request):
    return render (request,"addassistant.html")
def assistantmanagerlogin(request):
    return render(request,"assistantmanagerlogin.html")
def assistantmanagerdashboard(request):
    return render(request,"assistantmanagerdashboard.html")
def CustomerFee(request):
    return render(request,"customerfee.html")
def OtherAccounts(request):
    return render (request,"otheraccount.html")
def feeReport(request):
    return render(request,"fee-report.html")
def dueFee(request):
    return render(request,"duefee.html")
def SalaryReports(request):
    return render(request,"salaryreport.html")
def ExpenseReports(request):
    return render(request,"expense.html")
def ProfitReports(request):
    return render(request,"profit.html")
def DailyReports(request):
    return render(request,"dailyreports.html")
def weeklyReports(request):
    return render(request,"weeklyreport.html")
def YearlyReports(request):
    return render(request,"yearlyreport.html")
def fitnessReport(request):
    return render(request,"fitnessReport.html")
def backup(request):
    return render(request,"backup.html")
def Customer_SignUp(request):
    return render(request,"customerSignUp.html")