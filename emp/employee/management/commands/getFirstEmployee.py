from django.core.management import BaseCommand
from employee.models import Employee
class Command(BaseCommand):
    help='Get First Employee'

    def handle(self, *args, **options):
        first_emp = Employee.objects.first()
        self.stdout.write(f"First Employee in record is {first_emp}")