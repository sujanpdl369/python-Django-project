# from django.core.exceptions import ValidationError
from django import forms
# from .models import Accountant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Employee, Payment, Position

class UserStaffForm(UserCreationForm):
    email = forms.EmailField()
    admin_status = forms.BooleanField(required=False)
    class meta:
        model = User
        fields = ['email','username','password1','password2','admin_status']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already used")
        return email    
    
    def save(self, commit=True):
        user = super(UserStaffForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True
        if commit:
            user.save()
        return user
    
class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = "__all__"
    

class UserEmployeeForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ['email','username','password1','password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already used")
        return email
    
    def save(self, commit=True):
        user = super(UserEmployeeForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['pf_percent','accountant','position']
        
        
class UserEditForm(forms.ModelForm):
    email = forms.EmailField()
    # admin_status = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if(email == self.instance.email):
            print("No Validation Required.")
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already used")
        return email
    
    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  
    
class PaymentForm(forms.ModelForm):
    total_salary = forms.FloatField()
    class Meta:
        model = Payment
        fields = ['employee','total_salary','payment_month']
    
    def clean_total_salary(self):
        total_salary = self.cleaned_data.get('total_salary')
        if(total_salary<0.0):
            raise forms.ValidationError("Salary Cannot be Negative.")
        else:
            return total_salary
        
    def __init__(self,accountant,*args,**kwargs):
        super(PaymentForm,self).__init__(*args,**kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(accountant=accountant)
        self.fields['payment_month'].label = 'How much months Salary ? '