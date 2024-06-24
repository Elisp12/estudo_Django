from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name
    



class Parts(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparetion_steps = models.TextField()
    preparetion_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='parts/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null= True
    )
    author = models.ForeignKey(
       User , on_delete=models.SET_NULL, null= True
    )


# EDITED
# title description slug
# preparation_time preparation_time_unit
# services services_unit
# preparaion_step
# preparation_step_is_html
# created_at update_at
# is_published
# cover
# category (Relação)
# author (Relação)