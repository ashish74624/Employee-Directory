from django.urls import path
from . import views

app_name = 'employee_dir'

urlpatterns = [
    path('', views.employee_list , name="list"),
    path('create/', views.employee_create, name='create'),
    path('update/<path:slug>', views.employee_update, name='update'),
    path('delete/<path:slug>', views.employee_delete, name='delete'),
    path('<path:slug>', views.employee_page, name="page"),  # keep this last
]
