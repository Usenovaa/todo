from django.urls import path
from .views import task_list, create_task, task_update, task_delete, get_task_detail


urlpatterns = [
    path('tasks/', task_list),
    path('tasks-create/', create_task),
    path('tasks-update/<int:pk>/', task_update),
    path('tasks-delete/<int:pk>/', task_delete),
    path('tasks/<int:pk>/', get_task_detail)

]