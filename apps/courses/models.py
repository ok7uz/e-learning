from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['title']

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        db_table = 'section'
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['order']
        unique_together = (('course', 'title'),)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    section = models.ForeignKey(Section, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        db_table = 'lesson'
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        unique_together = (('section', 'title'),)

    def __str__(self):
        return self.title
