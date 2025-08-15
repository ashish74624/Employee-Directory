from django.urls import path
from . import views

app_name = 'employee_dir'

urlpatterns = [
    path('', views.employee_list , name="list"),
    path('<path:slug>', views.employee_page, name="page"),
]