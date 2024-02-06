from django.urls import path,include
from . import views

from accounts.views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserChangePasswordView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
    UserLogoutView,
)
urlpatterns = [

    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name='logout'),

    path("profile/", UserProfileView.as_view(), name="profile"),
    path("changepassword/", UserChangePasswordView.as_view(), name="changepassword"),
    path("send-reset-password-email/", SendPasswordResetEmailView.as_view(), name="send-reset-password-email"),
    path("reset-password/<str:uid>/<str:token>/", UserPasswordResetView.as_view(), name="reset-password"),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('register/google/',views.register_user_with_google, name='register_user_with_google'),
    path('login/google/', views.google_login, name='google-login'),
    # path('check-registration/', views.check_user_registration, name='check_user_registration'),


]
