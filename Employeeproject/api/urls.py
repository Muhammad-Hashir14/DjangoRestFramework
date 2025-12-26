from django.urls import path, include
from . import views

urlpatterns = [
    path("employees/", views.employees),
    path("employee/<int:pk>/", views.getEmployee),
    
    path('students/', views.Student.as_view()),
    path('student/<int:pk>/', views.getStudent.as_view())
]