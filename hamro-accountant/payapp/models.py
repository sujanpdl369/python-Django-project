from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Accountant(models.Model):
    is_admin = models.BooleanField(default=False)
    accountant = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.accountant}'
    
class Position(models.Model):
    position_name = models.CharField(max_length=50, unique=True)
    position_details = models.TextField(max_length=200)
    base_salary = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.position_name}'

class Employee(models.Model):
    position = models.ForeignKey(Position, on_delete= models.PROTECT)
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    accountant = models.ForeignKey(Accountant, on_delete= models.CASCADE)
    pf_percent = models.FloatField(default=10.0,validators=[MinValueValidator(10.0),MaxValueValidator(20.0)])    
    strip_account_id = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.employee}'
    
class Payment(models.Model):
    payment_pf_percent = models.FloatField(validators=[MinValueValidator(10.0),MaxValueValidator(20.0)])
    pf_amount = models.FloatField(validators=[MinValueValidator(0.0)])
    user_salary = models.PositiveIntegerField()    
    payment_month = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    paid_salary = models.FloatField(validators=[MinValueValidator(0.0)])
    payment_date = models.DateField()
    tax_amount = models.FloatField(validators=[MinValueValidator(0.0)])
    stripe_transaction_id = models.CharField(max_length=100,unique=True)
    accountant = models.ForeignKey(Accountant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.employee) +"  "+ self.stripe_transaction_id}'