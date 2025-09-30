from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView

from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from .tokens import account_activation_token

from academics.models import Teachers

# -------------------------------
# Registro de estudiantes
# -------------------------------
@extend_schema(request=UserRegisterSerializer, responses={201: UserSerializer})
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()  # estudiante por defecto inactivo
        uid = urlsafe_base64_encode(force_bytes(user.id_user))
        token = account_activation_token.make_token(user)

        activation_link = f"http://127.0.0.1:8000/api/auth/activate/{uid}/{token}/"
        subject = "Activa tu cuenta"
        message = f"Hola {user.name}, haz clic en el siguiente enlace para activar tu cuenta:\n{activation_link}"

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

# -------------------------------
# Activación de cuenta
# -------------------------------
@extend_schema(responses={200: {"message": "Cuenta activada exitosamente."}})
class ActivateAccountView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.status = "A"
            user.save()
            return Response({"message": "Cuenta activada exitosamente."}, status=status.HTTP_200_OK)
        return Response({"error": "Token inválido o expirado."}, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------
# Login
# -------------------------------
@extend_schema(request=UserLoginSerializer, responses={200: UserSerializer})
class LoginView(GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        return Response({
            "user": UserSerializer(user).data,
            "tokens": {"access": access, "refresh": str(refresh)},
        }, status=status.HTTP_200_OK)

# -------------------------------
# CRUD usuarios
# -------------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if getattr(self, "swagger_fake_view", False):
            return CustomUser.objects.none()
        if user.is_superuser or user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id_user=user.id_user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Usuario eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)

# -------------------------------
# Crear profesores (solo admin/staff)
# -------------------------------
@extend_schema(request=UserRegisterSerializer, responses={201: UserSerializer})
class CreateTeacherView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if not (user.is_superuser or user.is_staff):
            return Response({"error": "No tienes permisos para crear profesores."}, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        teacher_user = serializer.save()

        # Asignar rol profesor y activar
        teacher_user.id_role = 2
        teacher_user.is_active = True
        teacher_user.status = "A"
        teacher_user.save()

        return Response({
            "message": "Profesor creado correctamente.",
            "user": UserSerializer(teacher_user).data
        }, status=status.HTTP_201_CREATED)
 