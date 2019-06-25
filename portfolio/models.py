from django.db import models


class Technology(models.Model):
    title = models.CharField(max_length=100)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Technologies'


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='project_image')


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    images = models.ManyToManyField(ProjectImage, blank=True)