from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Appartement
from .serializers import AppartementSerializer
# Create your views here.


class ApartView(APIView):
    def get(self, request):
        Appartements = Appartement.objects.all()
        serializer = AppartementSerializer(Appartements, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = AppartementSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
class ApartViewID(APIView):
    def get(self, request,id):
        Appartements = Appartement.objects.filter(i)
        serializer = AppartementSerializer(Appartements, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = AppartementSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
