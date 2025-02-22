from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Announcement
from django.template.loader import render_to_string
import datetime
from django.utils import timezone


@shared_task
def send_email_task_new_respond(pk):
    """
    Отправка сообщения при создании отклика.
    :param pk: id сообщения на которое создали отклик.
    """
    instance = Announcement.objects.get(pk=pk)
    member = User.objects.get(username=instance.author)
    subject = f'Новый отклик к вашему объявлению "{instance.title}" от {instance.author}'
    text_content = (
        f'Новый отклик к вашему объявлению "{instance.title}" от {instance.author}\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000/{pk}'
    )
    html_content = (
        f'Заголовок: {instance.title}<br>'
        f'Новый отклик к вашему объявлению "{instance.title}" от {instance.author}<br><br>'
        f'<a href="http://127.0.0.1:8000{pk}">'
        f'Перейти</a>'
    )
    email = member.email
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_email_task_confirm_respond(pk, author):
    """
    Отправка сообщения при принятии отклика.
    :param pk: id сообщения на которое создали отклик.
    :param author: автор объявления.
    """
    instance = Announcement.objects.get(pk=pk)
    member = User.objects.get(username=author)
    subject = f'Ваш отклик к объявлению "{instance.title}" от {instance.author} принят.'
    text_content = (
        f'Ваш отклик к объявлению "{instance.title}" от {instance.author} принят.\n'
        f'Ссылка на публикацию: http://127.0.0.1:8000/{pk}'
    )
    html_content = (
        f'Заголовок: {instance.title}<br>'
        f'Ваш отклик к объявлению "{instance.title}" от {instance.author} принят.<br><br>'
        f'<a href="http://127.0.0.1:8000{pk}">'
        f'Перейти</a>'
    )
    email = member.email
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
def send_news_last_week():
    """
    Рассылка по расписанию.
    """
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Announcement.objects.filter(dateCreation__gte=last_week)
    subscribers = set(User.objects.all().values_list('email', flat=True))
    html_content = render_to_string('daily_post.html',
                                    {'link': settings.SITE_URL,
                                     'posts': posts})
    msg = EmailMultiAlternatives(
        subject="Объявления за  последнюю неделю",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()