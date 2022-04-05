from django.apps import AppConfig


class EatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eat'

class ItemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item'
