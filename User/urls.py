from django.urls import path
from . import views


urlpatterns = [

    path('set/all', views.UserAPIView.as_view()),

    path('set/<int:pk>', views.UserAPIViewID.as_view()),


]
