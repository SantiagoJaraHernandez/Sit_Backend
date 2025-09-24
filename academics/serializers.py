# academics/serializers.py
from rest_framework import serializers
from .models import (
    Semester, CutType, AcademicCut, AcademicCutGrades,
    ClassificationTypes, Course, CourseStudents, CourseTeachers,
    DataTrainModelPrediction, DataTestModelPrediction,
    ItemHeader, ItemResponseDetail, MslqItem, MslqResponse,
    OutputModelPrediction, StudentExerciseAttempts, Students, StudentsTasks,
    SupportExercise, SupportTopics, Task, TaskGrades, Teachers,
    TutoringTopic, TutoringGroup, TutoringParticipation
)

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"

class CutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CutType
        fields = "__all__"

class AcademicCutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCut
        fields = "__all__"

class AcademicCutGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicCutGrades
        fields = "__all__"

class ClassificationTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationTypes
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class CourseStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudents
        fields = "__all__"

class CourseTeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTeachers
        fields = "__all__"

class DataTrainModelPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTrainModelPrediction
        fields = "__all__"

class DataTestModelPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTestModelPrediction
        fields = "__all__"

class ItemHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemHeader
        fields = "__all__"

class MslqItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MslqItem
        fields = "__all__"

class MslqResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MslqResponse
        fields = "__all__"

class ItemResponseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemResponseDetail
        fields = "__all__"

class OutputModelPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputModelPrediction
        fields = "__all__"

class StudentExerciseAttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentExerciseAttempts
        fields = "__all__"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class StudentsTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsTasks
        fields = "__all__"

class SupportExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportExercise
        fields = "__all__"

class SupportTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTopics
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TaskGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGrades
        fields = "__all__"

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"

class TutoringTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringTopic
        fields = "__all__"

class TutoringGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringGroup
        fields = "__all__"

class TutoringParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutoringParticipation
        fields = "__all__"
