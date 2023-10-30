from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.course_name


class SchoolFacility(models.Model):
    facility_name = models.CharField(max_length=50)
    usage_purpose = models.TextField()

    def __str__(self):
        return self.facility_name


class Laboratory(SchoolFacility):
    equipment_list = models.TextField()

    def __str__(self):
        return self.facility_name
