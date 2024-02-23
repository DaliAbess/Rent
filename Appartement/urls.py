from django.urls import path
from . import views


urlpatterns = [

    path('set/', views.ApartView.as_view()),
    path('set/<int:id>', views.ApartViewID.as_view()),


]
