from django.db import models

# Create your models here.

class Subject(models.Model):
    sub_id = models.CharField(max_length=10)
    sub_name = models.CharField(max_length=64)
    sem = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.sub_id} : {self.sub_name} : {self.status} "

class Student(models.Model):
    stu_id = models.CharField(max_length=10)
    stu_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.stu_id} : {self.stu_name}"

class Apply(models.Model):
    stu_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stu_apply")
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="sub_apply")

    def __str__(self):
        return f"{self.stu_id} : {self.sub_id}"