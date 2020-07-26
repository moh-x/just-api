from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def test_view(request):
    data = {
        'name': 'Babatunde',
        'age': 21,
    }
    return JsonResponse(data)


def list_view(request):
    data = ['yu', 'gi', 'ho', 10]
    return JsonResponse(data, safe=False)
