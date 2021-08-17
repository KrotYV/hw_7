from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Generate random user\'s username, email and password'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, choices=range(1, 11), help='Number of users to create (from 1 to 10)')

    def handle(self, *args, **options):
        count = options['count']
        for i in range(count):
            User.objects.create_user(username=fake.user_name(), email=fake.email(), password=fake.password())
        self.stdout.write(self.style.SUCCESS(f'Successfully creat {count} users'))
