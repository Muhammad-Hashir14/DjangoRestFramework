from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register("staff", views.StaffView, basename = 'staff')

urlpatterns = [
    path("employees/", views.employees),
    path("employee/<int:pk>/", views.getEmployee),
    
    path('students/', views.Student.as_view()),
    path('student/<int:pk>/', views.getStudent.as_view()),
    
    # path("staff/", views.StaffView.as_view()),
    # path("staff/<int:pk>/", views.getStaff.as_view())
    path("", include(router.urls)),
    
    path("blogs/", views.BlogsView.as_view()),
    path("comments/", views.CommentView.as_view()),
    
    path("blogs/<int:pk>/", views.getBlog.as_view()),
    path("comments/<int:pk>/", views.getComment.as_view()),
    
    path("register/", views.RegisterView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]