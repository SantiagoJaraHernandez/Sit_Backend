# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateTeacherView, RegisterView, ActivateAccountView, LoginView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"

# Router para CRUD de usuarios
router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    # Registro de usuario
    path("register/", RegisterView.as_view(), name="register"),
    
    # Activación de cuenta
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    
    # Login con email y contraseña -> genera tokens JWT
    path("login/", LoginView.as_view(), name="login"),
    
    # Refresh de token JWT
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # CRUD de usuarios (list, update, delete, retrieve)
    path("", include(router.urls)),

    path("teachers/create/", CreateTeacherView.as_view(), name="create-teacher"),
]
