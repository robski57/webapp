from django.db import models

BEER_CHOICES = (
        ('D', 'Domestic'),
        ('I', 'Import'),
)

class Beer(models.Model):
        name            = models.CharField(max_length=200)
        slug            = models.SlugField(unique=True)
        brewery         = models.ForeignKey('Brewery')
        locality        = models.CharField(max_length=1, choices=BEER_CHOICES)
        description     = models.TextField(blank=True)
       # image1          = models.ImageField(upload_to="images/beerthumbs/", help_text="50x180px image")
        def __unicode__(self):
                return self.name

class Brewery(models.Model):
        name            = models.CharField(max_length=200)
        slug            = models.SlugField(unique=True)
        description     = models.TextField(blank=True)

        def __unicode__(self):
                return self.name
