from django.db import models
from movie_viewer.models import MovieViewer
# Create your models here.
from categories.models import CategoryModel
class MoviesModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.IntegerField()
    realis_date = models.DateTimeField()
    image = models.ImageField(upload_to="service/images/")
    is_favourite = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = "Movies"

   
