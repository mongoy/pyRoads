from django.contrib import admin
from .models import *


@admin.register(Road)
class RoadAdmin(admin.ModelAdmin):
    """Перечень дорог"""
    list_display = [field.name for field in Road._meta.fields]  # все поля выводит в цикле
    search_fields = ["nroad"]
    list_filter = ["nroad", "nregion"]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Перечень районов"""
    list_display = ("id", "name",)


@admin.register(TypeRoad)
class TypeRoadAdmin(admin.ModelAdmin):
    """Перечень типов дорог"""
    list_display = ("id", "name")


@admin.register(ElRoad)
class ElRoadAdmin(admin.ModelAdmin):
    """Перечень дорог"""
    list_display = [field.name for field in ElRoad._meta.fields]  # все поля выводит в цикле
    search_fields = ["nroad", "nelroad"]
    list_filter = ["nroad", "nregion", "nelroad"]


@admin.register(TypeElRoad)
class TypeElRoadAdmin(admin.ModelAdmin):
    """Перечень типов элементов дорог"""
    list_display = ("id", "name")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """Материал"""
    list_display = ("id", "name")