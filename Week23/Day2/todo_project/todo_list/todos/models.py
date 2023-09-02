from django.db import models


class Todo(models.Model):
    title = models.CharField()
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField()
    date_completion = models.DateField()
    deadline_date = models.DateField()
