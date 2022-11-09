from django.apps import AppConfig
from django.contrib import admin


class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
    verbose_name = 'Женщины мира'
