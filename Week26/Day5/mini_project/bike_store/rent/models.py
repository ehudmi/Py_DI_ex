from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)


class VehicleSize(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class RentalStation(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    address = models.CharField(max_length=50)


class VehicleAtRentalStation(models.Model):
    arrival_date = models.DateField(auto_now_add=True)
    departure_date = models.DateField(null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
