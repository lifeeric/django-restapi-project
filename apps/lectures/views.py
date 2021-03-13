from rest_framework import serializers, viewsets
from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('title', 'description', 'lecturer_name', 'date', 'duration', 'slides_url')


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
