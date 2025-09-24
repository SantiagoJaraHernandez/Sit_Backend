# academics/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SemesterViewSet, CutTypeViewSet, AcademicCutViewSet, AcademicCutGradesViewSet,
    ClassificationTypesViewSet, CourseViewSet, CourseStudentsViewSet, CourseTeachersViewSet,
    DataTrainModelPredictionViewSet, DataTestModelPredictionViewSet,
    ItemHeaderViewSet, ItemResponseDetailViewSet, MslqItemViewSet, MslqResponseViewSet,
    OutputModelPredictionViewSet, StudentExerciseAttemptsViewSet, StudentsViewSet, StudentsTasksViewSet,
    SupportExerciseViewSet, SupportTopicsViewSet, TaskViewSet, TaskGradesViewSet, TeachersViewSet,
    TutoringTopicViewSet, TutoringGroupViewSet, TutoringParticipationViewSet
)

router = DefaultRouter()

# ----------------- Académicos -----------------
router.register(r"semesters", SemesterViewSet, basename="semester")
router.register(r"cut-types", CutTypeViewSet, basename="cuttype")
router.register(r"academic-cuts", AcademicCutViewSet, basename="academiccut")
router.register(r"academic-cut-grades", AcademicCutGradesViewSet, basename="academiccutgrades")
router.register(r"classification-types", ClassificationTypesViewSet, basename="classificationtypes")

# ----------------- Cursos -----------------
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"course-students", CourseStudentsViewSet, basename="coursestudents")
router.register(r"course-teachers", CourseTeachersViewSet, basename="courseteachers")

# ----------------- Modelos de Predicción -----------------
router.register(r"data-train-models", DataTrainModelPredictionViewSet, basename="datatrain")
router.register(r"data-test-models", DataTestModelPredictionViewSet, basename="datatest")
router.register(r"output-model-predictions", OutputModelPredictionViewSet, basename="outputpredictions")

# ----------------- MSLQ -----------------
router.register(r"item-headers", ItemHeaderViewSet, basename="itemheaders")
router.register(r"mslq-items", MslqItemViewSet, basename="mslqitems")
router.register(r"mslq-responses", MslqResponseViewSet, basename="mslqresponses")
router.register(r"item-response-details", ItemResponseDetailViewSet, basename="itemresponsedetails")

# ----------------- Ejercicios y Tareas -----------------
router.register(r"student-exercise-attempts", StudentExerciseAttemptsViewSet, basename="studentexattempts")
router.register(r"support-exercises", SupportExerciseViewSet, basename="supportexercises")
router.register(r"support-topics", SupportTopicsViewSet, basename="supporttopics")
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"task-grades", TaskGradesViewSet, basename="taskgrades")
router.register(r"students", StudentsViewSet, basename="students")
router.register(r"students-tasks", StudentsTasksViewSet, basename="studentstasks")

# ----------------- Docentes -----------------
router.register(r"teachers", TeachersViewSet, basename="teachers")

# ----------------- Tutorías -----------------
router.register(r"tutoring-topics", TutoringTopicViewSet, basename="tutoringtopics")
router.register(r"tutoring-groups", TutoringGroupViewSet, basename="tutoringgroups")
router.register(r"tutoring-participation", TutoringParticipationViewSet, basename="tutoringparticipation")

urlpatterns = [
    path("", include(router.urls)),
]
