from django.urls import path
from NotesAPI import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('notes/',views.NotesList.as_view(),name='notes'),
    path("notes/<int:pk>/",views.NoteDetail.as_view(),name="note_detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
