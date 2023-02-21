from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import UserStaffForm, PositionForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from ..models import Accountant, Position
from django.views.generic import CreateView, ListView, DetailView, DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash



# Create your views here.

def index(request):
    return render(request, 'payapp/index.html');

def accountant_creation(request): 
    if request.method == "POST":
        user_form = UserStaffForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            accountant = user_form.save()
            Accountant.objects.create(accountant = accountant, is_admin=user_form.cleaned_data['admin_status'])
            print("accountant created sucessfully.")
            return redirect('payapp:login')
    elif request.method =="GET":
        user_form = UserStaffForm()
    context = {'user':user_form}
    return render(request, 'payapp/signup.html',context)
        
def login_user(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print('valid form')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("logged in")
                return redirect('payapp:index')
    elif request.method == "GET":
            form = AuthenticationForm()
    context = {'user':form}
    return render(request, 'payapp/login.html',context)


@method_decorator(login_required(login_url=reverse_lazy('payapp:login')),name="dispatch")
class PositionCreateView(CreateView,LoginRequiredMixin):
    model = Position
    form_class = PositionForm
    success_url = reverse_lazy('payapp:position_list')
    template_name = 'payapp/position_create.html'
    
@method_decorator(login_required(login_url=reverse_lazy('payapp:login')),name="dispatch")
class PositionListView(ListView):
    model = Position
    context_object_name = 'positions'
    # template_name = 'payapp/list_position.html'

@method_decorator(login_required(login_url=reverse_lazy('payapp:login')),name="dispatch")
class PositionDetailView(LoginRequiredMixin,DetailView):
    model = Position
    pk_url_kwarg= 'id'
    context_object_name='object'
    # template_name = "payapp/detail_position.html"

@method_decorator(login_required(login_url=reverse_lazy('payapp:login')),name="dispatch")
class PositionUpdateView(LoginRequiredMixin,UpdateView):
    model = Position
    form_class = PositionForm
    pk_url_kwarg= 'id'
    success_url = reverse_lazy('payapp:position_list')

    
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('payapp:index')


def change_password(request):
    if(request.method == "POST"):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('payapp:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'payapp/change_password.html', context)


def accountant_update(request):
    context = {}
    user = request.user
    if request.method == "GET":
        form = UserEditForm(instance=user)
        context['form'] = form
    elif request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        # print(form)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('payapp:index')
        context['form'] = form
    file_path = 'payapp/accountant_update.html'
    # file_path = 'payapp/update_accountant.html'
    return render(request,file_path,context)

def accountant_details(request):
    return render(request,'payapp/accountant_details.html')