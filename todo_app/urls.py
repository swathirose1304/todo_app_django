from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from todo_app.views import home , login_user, signup, add_todo, signout, delete_todo, change_todo

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('add-todo/', add_todo, name='add_todo'),
    path('delete-todo/<int:id>' , delete_todo ), 
    path('change-status/<int:id>/<str:status>' , change_todo ),
    path('logout/', signout, name='signout'),

]
