from rest_framework import generics
from .models import Worker
from .serializer import WorkerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
# class WorkerAPIView(generics.ListAPIView):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializercl

class WorkerAPIView(APIView):
    def get(self, request):
        lst = Worker.objects.all().values()
        return Response({'post': list(lst)})
    def post(self, request):
        post_new = Worker.objects.create(
            name=request.data["name"],
            second_name=request.data["second_name"],
            sportCategory=request.data["sportCategory"]
        )
        return Response({'post': model_to_dict(post_new)})