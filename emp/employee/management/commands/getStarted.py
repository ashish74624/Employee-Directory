from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Intro"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Name of the person who will be greated')

    def handle(self, *args, **options):
        name=options['name']

        self.stdout.write(f'Hello, {name} ')                