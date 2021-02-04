from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUp.as_view(),
         name="signup"),
    path("password_change/", views.ChangePassword,
         name="change_password"),
    path('password_reset/', views.PasswordResetView,
         name='password_reset'),
]
