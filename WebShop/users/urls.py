from django.urls import path
from .views import UserCreateView, UserLoginView, ChangePasswordView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
