from django.urls import path
from . import views

urlpatterns = [
    path('cluster/',views.cluster_data)
]
