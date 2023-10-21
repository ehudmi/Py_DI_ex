from django.db import models


class Category(models.Model):
    name = models.CharField()
    image = models.URLField()

    def __str__(self) -> str:
        return self.name


class Todo(models.Model):
    title = models.CharField()
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField()
    date_completion = models.DateField()
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, default=None, on_delete=models.DO_NOTHING)
