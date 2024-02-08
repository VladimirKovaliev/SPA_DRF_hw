from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_list = [
            {'username': 'user1', 'email': 'user1@sky.pro', 'phone': '+79254832848'},
            {'username': 'user2', 'email': 'user2@sky.pro', 'phone': '+78542386479'},
        ]
        user_for_create = []
        for user_item in user_list:
            user_for_create.append(User(**user_item))

        User.objects.bulk_create(user_for_create)
