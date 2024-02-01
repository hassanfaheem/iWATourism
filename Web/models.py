from uuid import uuid4
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from  embed_video.fields  import  EmbedVideoField
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
import os

FROM_CITIES = (
# UAE
    ('Abu Dhabi', 'Abu Dhabi'),
    ('Dubai', 'Dubai'),
    ('Sharjah', 'Sharjah'),
# India
    ('Bengaluru', 'Bengaluru'),
    ('Chennai', 'Chennai'),
    ('Mumbai', 'Mumbai'),
    ('Hyderabad', 'Hyderabad'),
    ('Lucknow', 'Lucknow'),
    ('Delhi', 'Delhi'),
    ('Jaipur', 'Jaipur'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Kolkata', 'Kolkata'),
    ('Thiruvananthapuram', 'Thiruvananthapuram')
)

TO_CITIES = (
# UAE
    ('Abu Dhabi', 'Abu Dhabi'),
    ('Dubai', 'Dubai'),
    ('Sharjah', 'Sharjah'),
# Georgia
    ('Tbilisi', 'Tbilisi')
)

ORDER_STATUS = (
    ('Processing', 'Processing'),
    ('Booked', 'Booked'),
)

PAYMENT_METHODS = (
    ('Debit/Credit Card', 'Debit/Credit Card'),
)

def upload_path(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email + ' - ' + self.first_name + ' ' + self.last_name

class GroupTour(models.Model):
    title = models.CharField(max_length=100)
    from_country = CountryField()
    to_country = CountryField()
    from_city = models.CharField(max_length=50, choices=FROM_CITIES, default='')
    to_city = models.CharField(max_length=50, choices=TO_CITIES, default='')
    days = models.SmallIntegerField(validators=[MaxValueValidator(50), MinValueValidator(1)])
    nights = models.SmallIntegerField(validators=[MaxValueValidator(50), MinValueValidator(1)])
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)
    description = RichTextField()
    included = models.TextField()
    not_included = models.TextField()
    total_seats = models.IntegerField()
    remaining_seats = models.IntegerField()
    booking_end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    sold_out = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Itinerary(models.Model):
    day = models.SmallIntegerField(validators=[MaxValueValidator(50), MinValueValidator(1)])
    date = models.DateField()
    description = RichTextField()
    group_tour = models.ForeignKey(GroupTour, on_delete=models.CASCADE)

class Package(models.Model):
    title = models.CharField(max_length=100)
    people = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group_tour = models.ForeignKey(GroupTour, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class AddOn(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group_tour = models.ForeignKey(GroupTour, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title}: +{self.price:,.0f}"

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact_number = models.CharField(max_length=25)
    alternative_contact_number = models.CharField(max_length=25)
    passport_number = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Booking(models.Model):
    group_tour = models.ForeignKey(GroupTour, on_delete=models.SET_NULL, blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, blank=True, null=True)
    add_on = models.ForeignKey(AddOn, on_delete=models.SET_NULL, blank=True, null=True)
    consent = models.BooleanField()
    total_amount = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    booking_amount = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)
    total_amount_paid = models.BooleanField(default=False)
    booking_amount_paid = models.BooleanField(default=False)
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=50, default='Debit/Credit Card')
    special_request = models.TextField(null=True, blank=True)
    status = models.CharField(choices=ORDER_STATUS, max_length=50, default='Processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.group_tour) + " - " + str(self.customer)
