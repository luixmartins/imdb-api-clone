from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
    
class Media(models.Model):
    TYPES = (
        ('movie', 'movie'),
        ('serie', 'serie'),
        ('documentary', 'documentary'),
        ('other', 'other'),
    )

    title = models.CharField(max_length=100, null=False, blank=False) 
    type_of = models.CharField(max_length=100, choices=TYPES, default='other', null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(null=False, blank=False)
    duration = models.PositiveIntegerField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='media', blank=True) 

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        

