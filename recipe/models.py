from django.db import models


TAG_TYPES = (
    ('CA', 'Category'),
    ('IN', 'Ingredient'),
    ('FL', 'Flavor'),
    ('EQ', 'Equipment'),
)


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    type = models.CharField(max_length=255, choices=TAG_TYPES)
    key = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.key