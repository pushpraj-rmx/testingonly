from django.contrib import admin
from django.urls import path
from myserver import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.get_post, name='list_create_employee'),
    path('',views.index),
    path('employees/<int:emp_id>/', views.delete_put, name='delete_update_employee'),
]
