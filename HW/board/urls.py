from tkinter.font import names

from django.urls import path

from . import views
from .views import AnnouncementList, AnnouncementDetail, AnnouncementCreate, AnnouncementEdit, AnnouncementDelete, \
    RespondList, RespondCreate, deleteRespond, confirmRespond

urlpatterns = [
    path('', AnnouncementList.as_view(), name='main'),
    path('<int:pk>', AnnouncementDetail.as_view(), name="detail"),
    path('create/', AnnouncementCreate.as_view(), name='announcement_add'),
    path('<int:pk>/edit/', AnnouncementEdit.as_view()),
    path('<int:pk>/delete/', AnnouncementDelete.as_view()),
    path('respond/', RespondList.as_view()),
    path('createRespond/<int:pk>', RespondCreate.as_view(), name='respond_add'),
    path('respond_delete/<int:id_respond>', deleteRespond, name='respond_delete'),
    path('respond_confirm/<int:id_respond>', confirmRespond, name='respond_confirm'),
]
