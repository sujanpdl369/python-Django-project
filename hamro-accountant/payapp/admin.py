from django.contrib import admin
from .models import Accountant, Payment, Position, Employee
# Register your models here.
admin.site.register(Accountant)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Payment)