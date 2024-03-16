from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from NotesAPI.models import Note
from NotesAPI.serializers import NoteSerializer

# Create your views here.
# @csrf_exempt
# def notes_list(request):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = NoteSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=200)
#         return JsonResponse(serializer.erros,status=400)

# @csrf_exempt    
# def note_detail(request,pk):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return JsonResponse(serializer.data)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = NoteSerializer(note,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=200)
#         return JsonResponse(serializer.errors,status=400)
    
#     elif request.method == "DELETE":
#         note.delete()
#         return HttpResponse(status=204)

class NotesList(APIView):
    def get(self,request,format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_REQUEST)
    

class NoteDetail(APIView):
    def get_object(self,pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Http404
    def get(self,request,pk,format=None):
        serializer = NoteSerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros,status=status.HTTP_400_REQUEST)
    
    def delete(self,request,pk,format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_400_REQUEST)

