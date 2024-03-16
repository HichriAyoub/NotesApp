from rest_framework import serializers
from NotesAPI.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'Name', 'text', 'date_created']

    def create(self, validated_data):
        return Note.objects.create(**validated_data)
    