from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# id (Integer, Primary Key)
# name (String)
# email (String, unique)
# phone number (PhoneNumberField) : PhoneNumberField provided by the django-phonenumber-field package.
# address (String)
class Person(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(region="IL")
    address = models.CharField()
