from django.shortcuts import render, redirect
from .models import Task

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth import logout, login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class CustomLoginView(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('task_list')

class CustomLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('task_list')

class RegisterForm(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterForm, self).form_valid(form)

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'base/todo_list.html'
    context_object_name = 'tasks'
    ordering = ['complet']
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        search = self.request.GET.get('search')
        if search :
            context['tasks'] = context['tasks'].filter(tiltel__icontains=search)
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'base/task_form.html'
    fields = ['tiltel','discription']
    success_url = reverse_lazy('task_list')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['tiltel','discription','complet']
    success_url = reverse_lazy('task_list')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')