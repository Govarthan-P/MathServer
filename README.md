# Ex.03 Design a Website for Server Side Processing
## Date:14/11/2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
nath.html

<html>
    <head>
        <title>my samplepage</title>
    </head>
    <body>
        <b><h1 align="center">Churn Rate Calculator</h1></b>
        <h2 align="center">Govarthan P(26014378)</h2>
        <form method="POST">
            {%csrf_token%}
            <label>Cust_Profit:</label>
            <input type="number" name="x" value="{{x}}"><br><br>
            <label>Cust_Lost:</label>
            <input type="number" name="y" value="{{y}}"><br><br>
            <input type="submit" value="calculate">
            <input type="reset"><br><br>
            <label>Churn:</label>
            <input type="number" name="churn" value="{{churn}}">
        </form> 
    </body>
</html>

views.py

from django.shortcuts import render
def calculateChurnRate(request):
    x = float(request.POST.get("x", '0'))
    y = float(request.POST.get("y", '0'))
    churn =  (( x-y) /x )*100 if request.method == 'POST' else 0
    print("cust_profit =",x)
    print("cust_lost =",y)
    print("churn_rate =",churn)
    return render(request, 'nathapp/nath.html',{'cust_profit': x, 'cust_lost': y, 'churn': churn })

urls.py

from django.contrib import admin
from django.urls import path
from nathapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculateChurnRate,name='calculateChurnRate'),
]
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (22).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (21).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
