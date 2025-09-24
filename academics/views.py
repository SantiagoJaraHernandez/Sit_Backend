# academics/views.py
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

from .models import (
    Semester, CutType, AcademicCut, AcademicCutGrades,
    ClassificationTypes, Course, CourseStudents, CourseTeachers,
    DataTrainModelPrediction, DataTestModelPrediction,
    ItemHeader, ItemResponseDetail, MslqItem, MslqResponse,
    OutputModelPrediction, StudentExerciseAttempts, Students, StudentsTasks,
    SupportExercise, SupportTopics, Task, TaskGrades, Teachers,
    TutoringTopic, TutoringGroup, TutoringParticipation
)
from .serializers import (
    SemesterSerializer, CutTypeSerializer, AcademicCutSerializer,
    AcademicCutGradesSerializer, ClassificationTypesSerializer, CourseSerializer,
    CourseStudentsSerializer, CourseTeachersSerializer, DataTrainModelPredictionSerializer,
    DataTestModelPredictionSerializer, ItemHeaderSerializer, ItemResponseDetailSerializer,
    MslqItemSerializer, MslqResponseSerializer, OutputModelPredictionSerializer,
    StudentExerciseAttemptsSerializer, StudentsSerializer, StudentsTasksSerializer,
    SupportExerciseSerializer, SupportTopicsSerializer, TaskSerializer, TaskGradesSerializer,
    TeachersSerializer, TutoringTopicSerializer, TutoringGroupSerializer, TutoringParticipationSerializer
)
from .permissions import IsAdmin, IsTeacherOrAdmin, ReadOnlyOrTeacherOrAdmin

# ----------------- DECORADOR SWAGGER -----------------
def add_swagger(viewset_class, tag_name):
    """
    Decorador para agregar descripciones y tags a todos los métodos de un ViewSet
    """
    class WrappedViewSet(viewset_class):
        @swagger_auto_schema(operation_description=f"Lista todos los {tag_name}.", tags=[tag_name])
        def list(self, request, *args, **kwargs):
            return super().list(request, *args, **kwargs)

        @swagger_auto_schema(operation_description=f"Crea un nuevo {tag_name[:-1]}.", tags=[tag_name])
        def create(self, request, *args, **kwargs):
            return super().create(request, *args, **kwargs)

        @swagger_auto_schema(operation_description=f"Obtiene un {tag_name[:-1]} por su ID.", tags=[tag_name])
        def retrieve(self, request, *args, **kwargs):
            return super().retrieve(request, *args, **kwargs)

        @swagger_auto_schema(operation_description=f"Actualiza un {tag_name[:-1]} existente por su ID.", tags=[tag_name])
        def update(self, request, *args, **kwargs):
            return super().update(request, *args, **kwargs)

        @swagger_auto_schema(operation_description=f"Elimina un {tag_name[:-1]} por su ID.", tags=[tag_name])
        def destroy(self, request, *args, **kwargs):
            return super().destroy(request, *args, **kwargs)

    return WrappedViewSet

# ----------------- VIEWS CATEGORIZADAS -----------------

# --- Académicos ---
SemesterViewSet = add_swagger(type('SemesterViewSet', (viewsets.ModelViewSet,), {
    'queryset': Semester.objects.all(),
    'serializer_class': SemesterSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Academics: Semesters')

CutTypeViewSet = add_swagger(type('CutTypeViewSet', (viewsets.ModelViewSet,), {
    'queryset': CutType.objects.all(),
    'serializer_class': CutTypeSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Academics: Cut Types')

AcademicCutViewSet = add_swagger(type('AcademicCutViewSet', (viewsets.ModelViewSet,), {
    'queryset': AcademicCut.objects.all(),
    'serializer_class': AcademicCutSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Academics: Academic Cuts')

AcademicCutGradesViewSet = add_swagger(type('AcademicCutGradesViewSet', (viewsets.ModelViewSet,), {
    'queryset': AcademicCutGrades.objects.all(),
    'serializer_class': AcademicCutGradesSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Academics: Academic Cut Grades')

ClassificationTypesViewSet = add_swagger(type('ClassificationTypesViewSet', (viewsets.ModelViewSet,), {
    'queryset': ClassificationTypes.objects.all(),
    'serializer_class': ClassificationTypesSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Academics: Classification Types')

# --- Cursos ---
CourseViewSet = add_swagger(type('CourseViewSet', (viewsets.ModelViewSet,), {
    'queryset': Course.objects.all(),
    'serializer_class': CourseSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Courses: Courses')

CourseStudentsViewSet = add_swagger(type('CourseStudentsViewSet', (viewsets.ModelViewSet,), {
    'queryset': CourseStudents.objects.all(),
    'serializer_class': CourseStudentsSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Courses: Students')

CourseTeachersViewSet = add_swagger(type('CourseTeachersViewSet', (viewsets.ModelViewSet,), {
    'queryset': CourseTeachers.objects.all(),
    'serializer_class': CourseTeachersSerializer,
    'permission_classes': [IsTeacherOrAdmin],
}), 'Courses: Teachers')

# --- Modelos de Predicción ---
DataTrainModelPredictionViewSet = add_swagger(type('DataTrainModelPredictionViewSet', (viewsets.ModelViewSet,), {
    'queryset': DataTrainModelPrediction.objects.all(),
    'serializer_class': DataTrainModelPredictionSerializer,
    'permission_classes': [IsTeacherOrAdmin],
}), 'ML Models: Data Train')

DataTestModelPredictionViewSet = add_swagger(type('DataTestModelPredictionViewSet', (viewsets.ModelViewSet,), {
    'queryset': DataTestModelPrediction.objects.all(),
    'serializer_class': DataTestModelPredictionSerializer,
    'permission_classes': [IsTeacherOrAdmin],
}), 'ML Models: Data Test')

OutputModelPredictionViewSet = add_swagger(type('OutputModelPredictionViewSet', (viewsets.ModelViewSet,), {
    'queryset': OutputModelPrediction.objects.all(),
    'serializer_class': OutputModelPredictionSerializer,
    'permission_classes': [IsTeacherOrAdmin],
}), 'ML Models: Output Predictions')

# --- MSLQ Items ---
ItemHeaderViewSet = add_swagger(type('ItemHeaderViewSet', (viewsets.ModelViewSet,), {
    'queryset': ItemHeader.objects.all(),
    'serializer_class': ItemHeaderSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'MSLQ: Item Headers')

MslqItemViewSet = add_swagger(type('MslqItemViewSet', (viewsets.ModelViewSet,), {
    'queryset': MslqItem.objects.all(),
    'serializer_class': MslqItemSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'MSLQ: Items')

MslqResponseViewSet = add_swagger(type('MslqResponseViewSet', (viewsets.ModelViewSet,), {
    'queryset': MslqResponse.objects.all(),
    'serializer_class': MslqResponseSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'MSLQ: Responses')

ItemResponseDetailViewSet = add_swagger(type('ItemResponseDetailViewSet', (viewsets.ModelViewSet,), {
    'queryset': ItemResponseDetail.objects.all(),
    'serializer_class': ItemResponseDetailSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'MSLQ: Response Details')

# --- Ejercicios y Tareas ---
StudentExerciseAttemptsViewSet = add_swagger(type('StudentExerciseAttemptsViewSet', (viewsets.ModelViewSet,), {
    'queryset': StudentExerciseAttempts.objects.all(),
    'serializer_class': StudentExerciseAttemptsSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Exercises: Student Attempts')

SupportExerciseViewSet = add_swagger(type('SupportExerciseViewSet', (viewsets.ModelViewSet,), {
    'queryset': SupportExercise.objects.all(),
    'serializer_class': SupportExerciseSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Exercises: Support Exercises')

SupportTopicsViewSet = add_swagger(type('SupportTopicsViewSet', (viewsets.ModelViewSet,), {
    'queryset': SupportTopics.objects.all(),
    'serializer_class': SupportTopicsSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Exercises: Support Topics')

TaskViewSet = add_swagger(type('TaskViewSet', (viewsets.ModelViewSet,), {
    'queryset': Task.objects.all(),
    'serializer_class': TaskSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Tasks: Tasks')

TaskGradesViewSet = add_swagger(type('TaskGradesViewSet', (viewsets.ModelViewSet,), {
    'queryset': TaskGrades.objects.all(),
    'serializer_class': TaskGradesSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Tasks: Grades')

StudentsViewSet = add_swagger(type('StudentsViewSet', (viewsets.ModelViewSet,), {
    'queryset': Students.objects.all(),
    'serializer_class': StudentsSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Students')

StudentsTasksViewSet = add_swagger(type('StudentsTasksViewSet', (viewsets.ModelViewSet,), {
    'queryset': StudentsTasks.objects.all(),
    'serializer_class': StudentsTasksSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Students: Tasks')

# --- Docentes ---
TeachersViewSet = add_swagger(type('TeachersViewSet', (viewsets.ModelViewSet,), {
    'queryset': Teachers.objects.all(),
    'serializer_class': TeachersSerializer,
    'permission_classes': [IsTeacherOrAdmin],
}), 'Teachers')

# --- Tutorías ---
TutoringTopicViewSet = add_swagger(type('TutoringTopicViewSet', (viewsets.ModelViewSet,), {
    'queryset': TutoringTopic.objects.all(),
    'serializer_class': TutoringTopicSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Tutoring: Topics')

TutoringGroupViewSet = add_swagger(type('TutoringGroupViewSet', (viewsets.ModelViewSet,), {
    'queryset': TutoringGroup.objects.all(),
    'serializer_class': TutoringGroupSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Tutoring: Groups')

TutoringParticipationViewSet = add_swagger(type('TutoringParticipationViewSet', (viewsets.ModelViewSet,), {
    'queryset': TutoringParticipation.objects.all(),
    'serializer_class': TutoringParticipationSerializer,
    'permission_classes': [ReadOnlyOrTeacherOrAdmin],
}), 'Tutoring: Participation')
