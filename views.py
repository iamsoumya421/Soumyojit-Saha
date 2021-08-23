from pickle import GET
from django.shortcuts import render
from django.http import HttpResponse,request
import joblib

def index(request):
    return render(request,'index.html')
def result(request):
        model=joblib.load("ranfor_model.sav")
        lis=[]
        """lis.append(request.GET['year'])
        lis.append(request.GET['km_driven'])
        lis.append(request.GET['fuel'])
        lis.append(request.GET['transmission'])
        lis.append(request.GET['owner'])
        lis.append(request.GET['mileage'])
        lis.append(request.GET['engine'])
        lis.append(request.GET['max_power'])
        lis.append(request.GET['seats'])"""
        year=request.GET['year']
        km=request.GET['km_driven']
        fuel_type=request.GET['fuel']
        transmission=request.GET['transmission']
        owner=request.GET['owner']
        mileage=request.GET['mileage']
        engine=request.GET['engine']
        max_power=request.GET['max_power']
        seats=request.GET['seats']

        """fuel_dict = {"Diesel": 0, "Petrol": 1, "CNG": 2, "LPG": 3}
        def get_val(val):
                for key, value in fuel_dict.items():
                        if val == key:
                                return value

        fuel=get_val(fuel)
        print(fuel)"""
        if fuel_type=='Diesel':
                fuel_type=0
        elif fuel_type=='Petrol':
                fuel_type=1
        elif fuel_type=='LPG':
                fuel_type=2
        else:
                fuel_type=3

        if transmission=="Manual":
                transmission=0
        else:
                transmission=1

        if owner=="First Owner":
                owner=0
        elif owner=="Second Owner":
                owner=1
        elif owner=="Third Owner":
                owner=2
        elif owner=="Fourth and Above Owner":
                owner=3
        else:
                owner=5

        #lis.append(year)
        lis.append(km)
        lis.append(fuel_type)
        lis.append(mileage)
        lis.append(engine)
        lis.append(seats)

        ans=0
        if ans!=0:
            ans=0
            ans = model.predict([lis])
        else:
                ans = model.predict([lis])
        ans=ans-200000
        ans=str(ans)[1:-1]
        return render(request,'result.html',{'ans':ans})



