from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "my test command help"

    def handle(self, *args, **options):
        self.stdout.write("Doing all the things")