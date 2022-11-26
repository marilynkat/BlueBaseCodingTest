from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "nintendo_drf.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import nintendo_drf.users.signals  # noqa F401
        except ImportError:
            pass
