from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Course Title")
    description = models.TextField(verbose_name="Course Description")
    duration = models.CharField(max_length=100, verbose_name="Duration (e.g. 3 months)")
    image = models.ImageField(upload_to="courses/", blank=True, null=True, verbose_name="Course Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

