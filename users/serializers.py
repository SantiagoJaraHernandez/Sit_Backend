from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser
from academics.models import Students
import random

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # NO incluir id_role: se asigna internamente
        fields = ["id_user", "name", "last_name", "email", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        # Rol y estado por defecto: estudiante
        validated_data["id_role"] = 1
        validated_data["is_active"] = False
        validated_data["status"] = "I"
        validated_data["is_staff"] = False
        validated_data["is_superuser"] = False

        user = super().create(validated_data)

        # Crear registro en Students si no existe
        if not Students.objects.filter(student_id=user.id_user).exists():
            code = f"S{random.randint(10000,99999)}"
            while Students.objects.filter(student_code=code).exists():
                code = f"S{random.randint(10000,99999)}"
            Students.objects.create(student_id=user.id_user, student_code=code)

        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado.")

        if not user.is_active:
            raise serializers.ValidationError("La cuenta no está activada.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Contraseña incorrecta.")

        data["user"] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id_user", "name", "last_name", "email", "status", "id_role", "is_active"]
