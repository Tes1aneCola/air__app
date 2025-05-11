from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from phonenumber_field import phonenumber

class User(AbstractUser):
    ROLE_CHOICES = (
    ('Guest', 'guest'),
    ('Host', 'host'),
       )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Guest')
    phone_number = models.CharField(32)
    avatar = models.ImageField()
class Property(models.Model):
    title = models.CharField()
    description = models.TextField()
    price_per_night = models.FloatField()
    city = models.CharField()
    address = models.CharField()
    PROPERTY_TYPE_CHOICES = [
        ('Apartment', 'apartment'),
        ('House', 'house'),
        ('Studio', 'Studio')
    ]
    RULE_CHOICES = (
    ('No smoking', 'no smoking'),
    ('Pets allowed', 'pets allowed'),
    )
    rule = models.CharField(max_length=12, choices=RULE_CHOICES)
    max_guests = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    owner  = models.ForeignKey(User, related_name="properties", on_delete=models.CASCADE)
    images  = models.ImageField()
    is_active = models.BooleanField(default=True)
class Booking(models.Model):
    property = models.ForeignKey(Property, related_name="bookings", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    STATUS_CHOICES = [
        ('Pending', 'pending'),
        ('Approved', 'approved'),
        ('Rejected', 'rejected'),
        ('Cancelled', 'cancelled'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
class Review(models.Model):
    property  = models.ForeignKey(Property, related_name="reviews", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class Amenity(models.Model):
    name = models.CharField(128)
    icon = models.ImageField()
    Property = models.ManyToManyField(Property)

