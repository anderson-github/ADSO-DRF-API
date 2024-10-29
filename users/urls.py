from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('sign-up/', views.SignUp.as_view(), name='sign_up'),
    path('login/', views.Login.as_view(), name='login'),
    path('my-profile/', views.Profile.as_view(), name='my-profile'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
