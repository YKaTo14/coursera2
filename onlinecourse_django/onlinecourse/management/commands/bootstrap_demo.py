"""Create demo content and a local admin user for the screenshots."""

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a demo admin user for the local Django project."

    def handle(self, *args, **options):
        User = get_user_model()
        user, created = User.objects.get_or_create(
            username="admin",
            defaults={"email": "admin@example.com"},
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password("admin123")
        user.save()
        if created:
            self.stdout.write(self.style.SUCCESS("Created admin/admin123"))
        else:
            self.stdout.write(self.style.SUCCESS("Updated admin/admin123"))
