from . import views
from django.urls import path

urlpatterns = [
    #path('', views.todo_list, name='todo_list'),
    path('', views.todo_list, name='todo_list'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('swap_element_title', views.swap_element_title, name='swap-element-title'),
    path('delete_todo/<int:pk>', views.del_todo, name='delete_todo'),
]