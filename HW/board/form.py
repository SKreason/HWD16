from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import request

from .models import Announcement


class AnnouncementForm(forms.ModelForm):
    author = User
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(min_length=10, label='Текст объявления', widget=forms.Textarea)
    category = forms.ChoiceField(
        label='Категория объявления:',
        choices=Announcement.CATEGORY,
    )
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'category', 'image', 'file']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть одинаковым с текстом новости"
            )

        return cleaned_data
