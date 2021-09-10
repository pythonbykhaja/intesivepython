from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Welcome to Django application')


def simple_interest(request):
    """
    This is the view for simple interest
    :param request: django.http.request object
    :return: simple interest calculated and formatted html output
    """
    principal = float(request.GET['principal'])
    time = float(request.GET['time'])
    rate = float(request.GET['rate'])
    si = principal * time * rate / 100
    response_text = f"<p> principal: {principal} <br/> time: {time} <br/> " \
                    f"rate: {rate}<br/> Simple Interest: {si}</p>"
    return HttpResponse(response_text)
