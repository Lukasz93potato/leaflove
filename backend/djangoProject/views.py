from django.http import JsonResponse
from django.shortcuts import render

def api_test(request):
    return JsonResponse({"message": "Hello from Django!"})

