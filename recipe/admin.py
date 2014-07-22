from django.contrib import admin

from recipe.models import Recipe
from recipe.models import Tag


class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    ordering = ('name',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('type', 'key',)
    ordering = ('type', 'key',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)