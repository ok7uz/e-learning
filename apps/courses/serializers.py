from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from .models import Course, Section, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(source='course.id', write_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'course_id', 'order']

    def create(self, validated_data):
        course_id = validated_data.pop('course')['id']
        course = get_object_or_404(Course, id=course_id)
        return Section.objects.create(**validated_data, course=course)


class CourseDetailSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'sections']


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price']
