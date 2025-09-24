from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from academics.models import Students, Teachers
import random

@receiver(post_save, sender=CustomUser)
def create_related_record(sender, instance, created, **kwargs):
    if not created:
        return

    # Estudiante
    if instance.id_role == 1:
        if not Students.objects.filter(student_id=instance.id_user).exists():
            code = f"S{random.randint(10000,99999)}"
            while Students.objects.filter(student_code=code).exists():
                code = f"S{random.randint(10000,99999)}"
            Students.objects.create(student_id=instance.id_user, student_code=code)

    # Profesor
    elif instance.id_role == 2:
        if not Teachers.objects.filter(teacher_id=instance.id_user).exists():
            Teachers.objects.create(teacher_id=instance.id_user, speciality="")
