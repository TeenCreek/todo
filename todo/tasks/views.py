from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('title', 'description', 'is_completed')
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_object(self):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])

        if task.author != self.request.user:
            raise Http404('Вы не можете просматривать эту задачу')

        return task


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('title', 'description', 'is_completed')
    template_name = 'tasks/task_form.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:task_list')

    def get_object(self):
        task = super().get_object()

        if task.author != self.request.user:
            raise Http404('Вы не можете изменять эту задачу')

        return task


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')

    def get_object(self):
        task = super().get_object()

        if task.author != self.request.user:
            raise Http404('Вы не можете удалить эту задачу')

        return task
