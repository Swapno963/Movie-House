from django.db import models
from movie_viewer.models import MovieViewer
from movies.models import MoviesModel
# Create your models here.
from django.contrib.auth.models import User

class Cart(models.Model):
    viewer = models.ForeignKey(User, on_delete = models.CASCADE)
    movie = models.ForeignKey(MoviesModel, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"Doctor : {self.viewer.user.first_name} , Patient : {self.movie.title}"
    

