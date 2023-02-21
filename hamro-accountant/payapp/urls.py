from django.urls import path, include
from payapp.views.accountant_and_position import (index,
                                                  PositionDetailView,
                                                  accountant_creation,
                                                  accountant_update,
                                                  login_user,
                                                  accountant_details,
                                                  change_password, 
                                                  PositionCreateView,
                                                  PositionListView,
                                                  PositionUpdateView,
                                                  logout_view
                                                  )

from payapp.views.employee import (employee_creation, 
                                   view_employee, 
                                   employee_update,
                                   employee_details,
                                #    payment_create,
                                    PayementCreateView,
                                   show_employee_balance,
                                   PaymentListView,
                                   view_transaction_details,
                                   UserListView,
                                   show_beruju,
                                   )
app_name="payapp"

urlpatterns = [
    # Home Page and others
    path('', index, name='index'),
    # Accountant Related
    path('accountant/create/',accountant_creation, name='accoutant_create'),
    path('accountant/update/self/',accountant_update, name='accountant_update'),
    path('accountant/details/', accountant_details, name='accountant_details'),
    # Position Related
    path('position/create/',PositionCreateView.as_view(), name='position_create'),
    path('position/',PositionListView.as_view(),name="position_list"),
    path('position/detail/<int:id>/', PositionDetailView.as_view(),  name="position_detail"),
    path('position/update/<int:id>/', PositionUpdateView.as_view(),name='position_update'),
    # Employee
    path('employee/create/', employee_creation, name='employee_create'),
    path('employee/',view_employee, name='employee_list'),
    path('employee/details/',employee_details, name='employee_details'),
    path('employee/update/self/',employee_update, name='employee_update'),
    # Authentication Related
    path('change-password/',change_password,name='change_password'),
    path('login/',login_user, name='login'),
    path('logout/',logout_view,name='logout'),
    # Payments related
    # path('payments/create/',payment_create,name='payment_create'),
    path("payments/create/",PayementCreateView.as_view(),name='payment_create'),
    path('payments/',PaymentListView.as_view(),name='payment_list'),
    # Employee balance
    path('balance/<int:id>/',show_employee_balance, name='balance'),
    #Salary Transaction
    path('transaction/<int:id>/',view_transaction_details,name='transaction'),
    # User list
    path('users/',UserListView.as_view(),name='users_list'),
    # Beruju
    path('beruju/<int:id>/',show_beruju,name='beruju_show')
]
