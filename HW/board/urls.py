from tkinter.font import names

from django.urls import path

from . import views
from .views import AnnouncementList, AnnouncementDetail, AnnouncementCreate, AnnouncementEdit, AnnouncementDelete, \
    RespondList

urlpatterns = [
    path('', AnnouncementList.as_view(), name='main'),
    path('<int:pk>', AnnouncementDetail.as_view(), name="detail"),
    path('create/', AnnouncementCreate.as_view(), name='announcement_add'),
    path('<int:pk>/edit/', AnnouncementEdit.as_view()),
    path('<int:pk>/delete/', AnnouncementDelete.as_view()),
    path('respond/', RespondList.as_view()),
]
