from django.db import models

# Create your models here.
from movie_viewer.models import MovieViewer
from movies.models import MoviesModel
from django.contrib.auth.models import User
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE)
    movie = models.ForeignKey(MoviesModel, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        # return f"Patient : {self.reviewer.user.first_name} ; Doctor {self.movie.title}"
        return self.body
 