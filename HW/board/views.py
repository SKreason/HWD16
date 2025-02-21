from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import RespondFilter
from .form import AnnouncementForm
from .models import Announcement, Respond


class AnnouncementList(ListView):
    model = Announcement
    ordering = '-dateCreation'
    template_name = 'main_list.html'
    context_object_name = 'Объявления'
    paginate_by = 5

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = AnnouncementFilter(self.request.GET, queryset)
    #     return self.filterset.qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Добавляем в контекст объект фильтрации.
    #     context['filterset'] = self.filterset
    #     return context


class AnnouncementDetail(DetailView):
    model = Announcement
    template_name = 'announcement.html'
    context_object_name = 'Объявление'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Отклики'] = Respond.objects.filter(announcement=self.kwargs['pk'])
        # создаем список существующих авторов и проверяем есть пользователь среди них
        return context


class AnnouncementCreate(PermissionRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'create.html'
    success_url = reverse_lazy('main')
    permission_required = ('board.add_announcement')
    raise_exception = True

    def form_valid(self, form):
        Announcement = form.save(commit=False)
        author = self.request.user  # Получаем текущего автора
        form.instance.author = author  # Устанавливаем автора
        Announcement.save()
        # send_email_task.delay(post.pk)
        return super().form_valid(form)


class AnnouncementEdit(PermissionRequiredMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'edit.html'
    success_url = reverse_lazy('main')
    permission_required = ('board.change_announcement')
    raise_exception = True


class AnnouncementDelete(PermissionRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    context_object_name = 'Объявление'
    permission_required = ('board.delete_announcement')
    raise_exception = True


class RespondList(ListView):
    model = Respond
    template_name = 'respond.html'
    context_object_name = 'Отклики'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = RespondFilter(self.request.GET, queryset, request=self.request.user)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        queryset = Respond.objects.all()
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        context['Объявления'] = Announcement.objects.filter(author=self.request.user)
        return context


def index(request):
    return render (request, 'sample.html')