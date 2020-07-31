from django.shortcuts import render
from django.http import JsonResponse


# Third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


# Create your views here.


class TestView(APIView):
    # def get(self, request, *args, **kwargs):
    #     data = {
    #         'name': 'Babatunde',
    #         'age': 21,
    #     }
    #     return Response(data)

    # Now get() using serializers

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # To pass in a single instance of the object,
        # We do post = qs.first()
        # And pass post below without the many= keyword.
        serializer = PostSerializer(qs, many=True)
        # We do not need to check is_valid(),
        # Since we are not passing the data= keyword.
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Just ordinary stuff without serializers
def test_view(request):
    data = {
        'name': 'Babatunde',
        'age': 21,
    }
    return JsonResponse(data)


# To pass a data type other than dict,
# Keyword safe=False must be passed.
def list_view(request):
    data = ['yu', 'gi', 'ho', 10]
    return JsonResponse(data, safe=False)
