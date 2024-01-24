from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = "Movie Category "