from django.shortcuts import render
def calculateChurnRate(request):
    x = float(request.POST.get("x", '0'))
    y = float(request.POST.get("y", '0'))
    churn =  (( x-y) /x )*100 if request.method == 'POST' else 0
    print("cust_profit =",x)
    print("cust_lost =",y)
    print("churn_rate =",churn)
    return render(request, 'nathapp/nath.html',{'cust_profit': x, 'cust_lost': y, 'churn': churn })
