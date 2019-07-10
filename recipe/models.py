# coding: utf-8
from django.db import models


class Recipe(models.Model):
    gousto_reference = models.PositiveIntegerField(blank=False, null=False)
    title = models.CharField(max_length=160, blank=False, null=False)
    short_title = models.CharField(max_length=80, blank=True, null=True)
    calories_kcal = models.PositiveIntegerField(blank=False, null=False, default=0)
    protein_grams = models.PositiveIntegerField(blank=False, null=False, default=0)
    fat_grams = models.PositiveIntegerField(blank=False, null=False, default=0)
    carbs_grams = models.PositiveIntegerField(blank=False, null=False, default=0)
    bulletpoint1 = models.CharField(max_length=30, blank=True, null=True)
    bulletpoint2 = models.CharField(max_length=30, blank=True, null=True)
    bulletpoint3 = models.CharField(max_length=30, blank=True, null=True)
    recipe_diet_type_id = models.CharField(max_length=20, blank=False, null=False)
    season = models.CharField(max_length=10, blank=False, null=False, default="all")
    base = models.CharField(max_length=30, blank=False, null=False)
    protein_source = models.CharField(max_length=30, blank=False, null=False)
    preparation_time_minutes = models.PositiveIntegerField(blank=False, null=False)
    shelf_life_days = models.PositiveIntegerField(blank=False, null=False)
    equipment_needed = models.CharField(max_length=30, blank=False, null=False)
    origin_country = models.CharField(max_length=30, blank=False, null=False)
    recipe_cuisine = models.CharField(max_length=30, blank=False, null=False)
    in_your_box = models.TextField(blank=True, null=True)
    box_type = models.CharField(max_length=30, blank=False, null=False)
    marketing_description = models.TextField()
    slug = models.SlugField(blank=False, null=False, max_length=150)
    created_at = models.DateTimeField(blank=False, null=False)
    updated_at = models.DateTimeField(blank=False, null=False)

    class Meta:
        db_table = "recipe"
        verbose_name = "recipe"
        verbose_name_plural = "recipes"

    def __str__(self):
        name = self.short_title or self.title
        return name
