from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Visite
from .serializers import VisiteSerializer


class VisiteListCreateAPIView(APIView):
    def get(self, request):
        visites = Visite.objects.all()
        serializer = VisiteSerializer(visites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VisiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VisiteRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Visite.objects.get(pk=pk)
        except Visite.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        visite = self.get_object(pk)
        serializer = VisiteSerializer(visite)
        return Response(serializer.data)

    def put(self, request, pk):
        visite = self.get_object(pk)
        serializer = VisiteSerializer(visite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        visite = self.get_object(pk)
        visite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
