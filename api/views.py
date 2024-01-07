from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from note.models import Note

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'All': '/all/',
        'Add': '/add/',
        'Detail': '/detail/<int:pk>/',
        'Edit': '/edit/<int:pk>/',
        'Delete': '/delete/<int:pk>/', 
    }
    
    return Response(api_urls)

@api_view(['GET'])
def AllNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def AddNote(request):
    if request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description')
        }
        serializer = NoteSerializer(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def DetailNote(request, pk):
    note = Note.objects.get(pk = pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def EditNote(request, pk):
    note = Note.objects.get(pk = pk)
    serializer = NoteSerializer(instance = note, data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteNote(request, pk):
    note = Note.objects.get(pk = pk)
    note.delete()
    return Response('Note deleted successfully.')