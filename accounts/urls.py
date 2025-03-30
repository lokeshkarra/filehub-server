from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)
from .views import UserRegistrationView, UserProfileView

urlpatterns = [
    # Authentication Endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
