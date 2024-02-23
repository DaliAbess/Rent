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
        Appartements = Appartement.objects.filter(id=id)
        serializer = AppartementSerializer(Appartements, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = AppartementSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            appartement = Appartement.objects.get(id=id)
        except Appartement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppartementSerializer(appartement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            appartement = Appartement.objects.get(id=id)
        except Appartement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        appartement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
