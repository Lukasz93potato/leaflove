from django.http import JsonResponse
from django.shortcuts import render

def api_test(request):
    return JsonResponse({"message": "Hello from Django!"})

def login_page(request):
    return render(request, "login.html")