# academics/models.py
from django.db import models

class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_level = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = "semester"
        managed = False

class CutType(models.Model):
    cut_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "cut_type"
        managed = False

class AcademicCut(models.Model):
    academic_cut_id = models.AutoField(primary_key=True)
    semester_id = models.IntegerField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, default="Active")
    cut_type_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "academic_cut"
        managed = False

class AcademicCutGrades(models.Model):
    academic_cut_grade_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    academic_cut_id = models.IntegerField()
    delivery_time = models.DateTimeField(null=True, blank=True)
    grade = models.DecimalField(max_digits=2, decimal_places=1)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "academic_cut_grades"
        managed = False

class ClassificationTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "classification_types"
        managed = False

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    semester_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    credits = models.IntegerField(default=3)

    class Meta:
        db_table = "course"
        managed = False

class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_code = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "students"
        managed = False


class CourseStudents(models.Model):
    course_student_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    student_id = models.IntegerField()
    enrollment_date = models.DateTimeField(null=True, blank=True)
    final_grade = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "course_students"
        managed = False

class CourseTeachers(models.Model):
    course_teacher_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    teacher_id = models.IntegerField()
    assignment_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "course_teachers"
        managed = False

class DataTrainModelPrediction(models.Model):
    data_train_model_prediction_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField(null=True, blank=True)
    type_id = models.IntegerField(null=True, blank=True)
    # item1..item36
    item1 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item2 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item3 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item4 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item5 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item6 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item7 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item8 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item9 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item10 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item11 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item12 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item13 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item14 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item15 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item16 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item17 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item18 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item19 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item20 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item21 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item22 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item23 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item24 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item25 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item26 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item27 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item28 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item29 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item30 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item31 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item32 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item33 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item34 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item35 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    item36 = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    c1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    c2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    c3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    n_final = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    class Meta:
        db_table = "data_train_model_prediction"
        managed = False

class DataTestModelPrediction(DataTrainModelPrediction):
    class Meta:
        db_table = "data_test_model_prediction"
        managed = False

class ItemHeader(models.Model):
    item_header_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "item_header"
        managed = False

class MslqItem(models.Model):
    mslq_item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    item_number = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "mslq_item"
        managed = False

class MslqResponse(models.Model):
    mslq_response_id = models.AutoField(primary_key=True)
    course_student_id = models.IntegerField()
    total_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    response_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "mslq_response"
        managed = False

class ItemResponseDetail(models.Model):
    item_response_detail_id = models.AutoField(primary_key=True)
    mslq_response_id = models.IntegerField(null=True, blank=True)
    mslq_item_id = models.IntegerField(null=True, blank=True)
    response_date = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "item_response_detail"
        managed = False

class OutputModelPrediction(models.Model):
    output_model_prediction_id = models.AutoField(primary_key=True)
    course_student_id = models.IntegerField(null=True, blank=True)
    academic_cut_id = models.IntegerField(null=True, blank=True)
    n_final_pred = models.DecimalField(max_digits=5, decimal_places=2)
    confidence_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    model_version = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "output_model_prediction"
        managed = False

class StudentExerciseAttempts(models.Model):
    student_exercise_attempt_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(null=True, blank=True)
    support_exercise_id = models.IntegerField(null=True, blank=True)
    attempt_date = models.DateTimeField(null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    execution_time_ms = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    code_submitted = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "student_exercise_attempts"
        managed = False

class StudentsTasks(models.Model):
    students_task_id = models.IntegerField(primary_key=True)
    students_student_id = models.IntegerField()
    task_task_id = models.IntegerField()

    class Meta:
        db_table = "students_tasks"
        managed = False

class SupportExercise(models.Model):
    support_exercise_id = models.AutoField(primary_key=True)
    assignment_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200)
    statement = models.TextField()
    difficulty_level = models.IntegerField()
    number_of_tries = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "support_exercise"
        managed = False

class SupportTopics(models.Model):
    support_topic_id = models.AutoField(primary_key=True)
    academic_cut_id = models.IntegerField(null=True, blank=True)
    topic = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Active")

    class Meta:
        db_table = "support_topics"
        managed = False

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    course_teacher_id = models.IntegerField()
    academic_cut_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, default="Active")
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        db_table = "task"
        managed = False

class TaskGrades(models.Model):
    task_grade_id = models.AutoField(primary_key=True)
    students_task_id = models.IntegerField()
    delivery_time = models.DateTimeField(null=True, blank=True)
    results = models.TextField(null=True, blank=True)
    grade = models.DecimalField(max_digits=2, decimal_places=1)
    status = models.CharField(max_length=10, default="Active")

    class Meta:
        db_table = "task_grades"
        managed = False

class Teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    speciality = models.CharField(max_length=100)

    class Meta:
        db_table = "teachers"
        managed = False

class TutoringTopic(models.Model):
    tutoring_topic_id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="Active")

    class Meta:
        db_table = "tutoring_topic"
        managed = False

class TutoringGroup(models.Model):
    tutoring_group_id = models.AutoField(primary_key=True)
    course_teacher_id = models.IntegerField(null=True, blank=True)
    tutoring_topic_id = models.IntegerField(null=True, blank=True)
    tutoring_date = models.DateField()
    tutoring_hour = models.TimeField()
    tutoring_site = models.TextField(null=True, blank=True)
    tutoring_message = models.TextField(null=True, blank=True)
    date = models.DateField()
    status = models.CharField(max_length=20, default="Schedule")

    class Meta:
        db_table = "tutoring_group"
        managed = False

class TutoringParticipation(models.Model):
    tutoring_participation_id = models.AutoField(primary_key=True)
    tutoring_group_id = models.IntegerField(null=True, blank=True)
    course_student_id = models.IntegerField(null=True, blank=True)
    enrollment_date = models.DateTimeField(null=True, blank=True)
    participation_status = models.CharField(max_length=15, default="Active")

    class Meta:
        db_table = "tutoring_participation"
        managed = False
