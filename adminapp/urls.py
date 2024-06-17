from django.urls import path
from . import views

urlpatterns = [
    path('admin_interface/',views.admin_interface,name='admin_home'),
    path('create_user/', views.createuser, name='createuser'),
    path('admin_search/',views.admin_search, name = 'admin_search'),
    path('delete_user/<id>/',views.delete_user, name = 'delete_user'),
    path('edit_user/<id>',views.edit_user, name = 'edit_user'),
]