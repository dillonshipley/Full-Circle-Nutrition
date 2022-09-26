import requests
from django.http import JsonResponse
from django.shortcuts import render
import logging

def index(request) -> JsonResponse:
    return JsonResponse(data={"response": "Thanks for hitting the recipes api index!"})

def health() -> JsonResponse:
    response = dict()

    # TODO Ping the database to see if its up

    # TODO Ping the frontend to see if it up
    res = requests.get()

    return JsonResponse(data=response)