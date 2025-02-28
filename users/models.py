from django.db import models

class Cse23_27(models.Model):
    id = models.AutoField(primary_key=True)
    enroll_no = models.IntegerField()
    register_number = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name
