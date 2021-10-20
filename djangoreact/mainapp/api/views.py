from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response

class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{'id':1, 'name':'Name1'}, {'id':2, 'name':'Name2'}]
        return Response(data)