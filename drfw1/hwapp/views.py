from xml.dom import ValidationErr
from django.shortcuts import render
from datetime import date
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Store
from .serializers import StoreSerializer
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView 

@api_view(http_method_names=['GET'])
def telldate(request):
    current_date = date.today()
    return_dict = {
        "date" : current_date,
        "year" : current_date.year,
        "month" : current_date.month,
        "day" : current_date.day
    }
    return Response(return_dict)

@api_view(http_method_names=['GET'])
def hello_world(request):
    return_dict = {"msg": "hello_world"}
    return Response(return_dict)

@api_view(http_method_names=['GET'])
def my_name(request, name_of_hacker):
    return_dict = {"msg": name_of_hacker}
    return Response(return_dict)

@api_view(http_method_names=['POST'])
def calculator(request):
    print(request.data["action"])
    calc = request.data
    if isinstance(calc["number1"], (float, int)) and isinstance(calc["number1"], (float, int)):
        if calc["action"] == "plus":
            res = float(calc["number1"])+float(calc["number2"])
        elif calc["action"] == "minus":
            res = float(calc["number1"])-float(calc["number2"])
        elif calc["action"] == "divide":
            if calc["number2"] != 0:
                res = float(calc["number1"])/float(calc["number2"])
            else:
                raise ZeroDivisionError
        elif calc["action"] == "multiply":
            res = float(calc["number1"])*float(calc["number2"])
        else:
            raise ValidationErr
    else:
        raise ValidationErr
        
    return Response({"result": res})


class StoreAPIView(APIView):
    def get(self, request, format=None):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)

