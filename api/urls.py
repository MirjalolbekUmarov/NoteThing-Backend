from django.urls import path
from .views import ApiOverview, AllNotes, AddNote, EditNote, DeleteNote, DetailNote

urlpatterns = [
    path('', ApiOverview),
    path('note/all/', AllNotes),
    path('note/add/', AddNote),
    path('note/edit/<int:pk>/', EditNote),
    path('note/delete/<int:pk>/', DeleteNote),
    path('note/detail/<int:pk>/', DetailNote)
]