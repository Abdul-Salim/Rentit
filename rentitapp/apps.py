from django.apps import AppConfig


class RentitappConfig(AppConfig):
    name = 'rentitapp'
    def ready(self):
        import rentitapp.signals
