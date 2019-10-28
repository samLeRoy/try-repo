from django.urls import path
from .views import project_index, project_detail

urlpatterns = [
    path('projects/', project_index, name='project_index'),
    path('<int:pk>/', project_detail, name='project_detail'),
]
