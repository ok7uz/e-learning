from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Course, Section, Lesson
from .serializers import CourseListSerializer, CourseDetailSerializer, SectionSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

    @extend_schema(
        responses={
            200: CourseListSerializer(many=True),
        }
    )
    def list(self, request, *args, **kwargs):
        queryset = Course.objects.all()
        serializer = CourseListSerializer(queryset, many=True)
        return Response(serializer.data)


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
