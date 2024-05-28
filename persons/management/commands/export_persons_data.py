import csv

from django.core.management.base import BaseCommand

from persons.models import Persons


class Command(BaseCommand):
    help = 'Export persons data to CSV file'

    def handle(self, *args, **kwargs):
        persons = Persons.objects.prefetch_related('skills', 'position').all()

        with open('persons_data.csv', 'w', encoding='utf-8', newline='') as csvfile:
            fieldnames = ['Lp.', 'Imię', 'Nazwisko', 'Umiejętności', 'Pozycja']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for idx, person in enumerate(persons, start=1):

                writer.writerow({
                    'Lp.': idx,
                    'Imię': person.first_name,
                    'Nazwisko': person.last_name,
                    'Umiejętności': ', '.join(skill.name for skill in person.skills.all()),
                    'Pozycja': person.position.name if person.position else ''
                })

        self.stdout.write(self.style.SUCCESS('Successfully exported persons data to persons_data.csv'))
