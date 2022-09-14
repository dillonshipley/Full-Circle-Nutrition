from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return JsonResponse(data={"response": "Thanks for hitting the recipes api index!"})

