from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Announcement(models.Model):
    CATEGORY = [
        ('MT', 'Танки'),
        ('HS', 'Хилы'),
        ('DD', 'ДД'),
        ('TR', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', 'Квестгиверы'),
        ('BS', 'Кузнецы'),
        ('SR', 'Кожевники'),
        ('PM', 'Зельевары'),
        ('SM', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField()
    category = models.CharField(choices=CATEGORY, max_length=2, default='TR', verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/', blank=True)
    file = models.FileField(upload_to='file/', blank=True)

    def __str__(self):
        return f'{self.id} {self.title}'

    def preview(self):
        return f'{self.text[0: 124]}...'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Respond(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

