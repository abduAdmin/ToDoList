from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',RegisterForm.as_view(),name='register'),

    path('',TaskList.as_view(),name='task_list'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task_detail'),
    path('task_form/',TaskCreate.as_view(),name='task_form'),
    path('task_update/<int:pk>/',TaskUpdate.as_view(),name='task_update'),
    path('task_delete/<int:pk>/',TaskDelete.as_view(),name='task_delete'),
    path('logout/', LogoutView.as_view(next_page='task_list'), name='logout'),
    path('logout_/',CustomLogoutView.as_view(),name='logout'),
]