from django.db import models

# Create your models here.

class Pokeyman(models.Model):

    name = models.CharField(max_length=128)

    def __repr__(self) -> str:
        return self.name
