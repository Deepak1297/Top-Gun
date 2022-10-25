from django.urls import path
from .views import TaskList, TaskDetails, CreateTasks, UpdateTasks, DeleteView, CustomLogin, RegisterationPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterationPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetails.as_view(), name='task'),
    path('create-task/', CreateTasks.as_view(), name='task-create'),
    path('task-update/<int:pk>/', UpdateTasks.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
