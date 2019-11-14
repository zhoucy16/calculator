from django.shortcuts import render
from django.http import HttpResponse

def calculate(request):
    formula = request.GET['formula']
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'
    return HttpResponse(result)