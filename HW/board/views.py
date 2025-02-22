from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import RespondFilter
from .form import AnnouncementForm, RespondForm
from .models import Announcement, Respond
from .tasks import send_email_task_new_respond, send_email_task_confirm_respond


class AnnouncementList(ListView):
    """
    Представление для списка объявлений.
    """
    model = Announcement
    ordering = '-dateCreation'
    template_name = 'main_list.html'
    context_object_name = 'Объявления'
    paginate_by = 5


class AnnouncementDetail(DetailView):
    """
    Представление для объявления.
    """
    model = Announcement
    template_name = 'announcement.html'
    context_object_name = 'Объявление'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Отклики'] = Respond.objects.filter(announcement=self.kwargs['pk'])
        return context


class AnnouncementCreate(PermissionRequiredMixin, CreateView):
    """
    Представление для создания объявления.
    """
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
        return super().form_valid(form)


class AnnouncementEdit(PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования объявления.
    """
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'edit.html'
    success_url = reverse_lazy('main')
    permission_required = ('board.change_announcement')
    raise_exception = True


class AnnouncementDelete(PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления объявления.
    """
    model = Announcement
    template_name = 'delete.html'
    success_url = reverse_lazy('main')
    context_object_name = 'Объявление'
    permission_required = ('board.delete_announcement')
    raise_exception = True


class RespondList(ListView):
    """
    Представление для списка откликов.
    """
    model = Respond
    template_name = 'respond.html'
    context_object_name = 'Отклики'
    ordering = "-announcement"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = RespondFilter(self.request.GET, queryset, request=self.request.user)
        return self.filter.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        context['Объявления'] = Announcement.objects.filter(author=self.request.user)
        return context


class RespondCreate(PermissionRequiredMixin, CreateView):
    """
    Представление для создания отклика.
    """
    model = Respond
    form_class = RespondForm
    template_name = 'createRespond.html'
    success_url = reverse_lazy('main')
    permission_required = ('board.add_respond')
    raise_exception = True

    def form_valid(self, form):
        Respond = form.save(commit=False)
        author = self.request.user  # Получаем текущего автора
        form.instance.member = author  # Устанавливаем автора
        form.instance.announcement = Announcement.objects.get(id=self.kwargs['pk'])
        Respond.save()
        send_email_task_new_respond(Respond.announcement_id)
        return super().form_valid(form)

def deleteRespond(request, id_respond):
    """
    Удаление отклика.
    :param request: запрос на удаление.
    :param id_respond: ID отклика.
    :return: ссылка на страницу откликов.
    """
    Respond.objects.get(id=id_respond).delete()
    return redirect(f'/respond/')


def confirmRespond(request, id_respond):
    """
    Принятие отклика.
    :param request: запрос на принятие.
    :param id_respond: ID отклика.
    :return: ссылка на страницу откликов.
    """
    respond = Respond.objects.get(id=id_respond)
    respond.confirm = 1
    respond.save()
    send_email_task_confirm_respond(respond.announcement_id, respond.member)
    return redirect(f'/respond/')
