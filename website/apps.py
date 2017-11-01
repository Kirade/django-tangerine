from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'

    # This will trigger the @receiver decorator in singals.py
    def ready(self):
        import website.signals
