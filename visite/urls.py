from django.urls import path
from . import views


urlpatterns = [

    path('set/all', views.VisiteListCreateAPIView.as_view()),

    path('set/<int:pk>', views.VisiteRetrieveUpdateDestroyAPIView.as_view()),


]
