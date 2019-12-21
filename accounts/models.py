from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Users(models.Model):
    """
    Model defining patients/customers who use the site to book
    """
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    phone = PhoneNumberField()
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    personnumber = models.CharField(max_length = 12)

    def __str__(self):
        return self.fname

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

class RegUsers(models.Model):
    """
    model defining paid users of the site
    """
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    phone_number = PhoneNumberField()
    personnumber = models.CharField(max_length = 12)

    def __str__(self):
        return self.fname

    class Meta:
        verbose_name = 'Registered Users'
        verbose_name_plural = 'Registered Users'


class Clinic(models.Model):
    """
    Model defining clinic details for registered clinics
    """
    name = models.CharField(max_length = 50)
    phone_number = PhoneNumberField()
    street = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    postno = models.CharField(max_length = 50)
    owner = models.ForeignKey(RegUsers, on_delete=models.CASCADE)
    patients = models.ManyToManyField(Users)

    def __str__(self):
        return self.name
