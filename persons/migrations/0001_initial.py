# Generated by Django 5.0.6 on 2024-05-24 13:18

import django.db.models.deletion
from django.db import migrations, models
from django.db import transaction
from faker import Faker
from typing import Generator

import random

fake = Faker("pl_PL")

_skills = [
    "Python", "Django", "Java", "JavaScript", "Html", "Css", "Flask", "Htmx", "Linux"
]


def _unique_positions() -> Generator:
    positions = []
    while len(positions) < 20:
        job = fake.job()
        if job not in positions:
            yield job
            positions.append(job)


@transaction.atomic()
def fill_models_with_data(apps, *args, **kwargs) -> None:
    Skills = apps.get_model('persons', 'Skills')  # noqa
    Position = apps.get_model('persons', 'Position')  # noqa
    Persons = apps.get_model('persons', 'Persons')  # noqa

    positions_to_create = []
    for position in _unique_positions():
        positions_to_create.append(Position(name=position))

    Position.objects.bulk_create(positions_to_create)

    skills_to_create = []
    for skill in _skills:
        skills_to_create.append(Skills(name=skill))

    Skills.objects.bulk_create(skills_to_create)

    persons_to_create = []
    for _ in range(100):
        persons_to_create.append(
            Persons(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                position=random.choice(positions_to_create),
            )
        )

    Persons.objects.bulk_create(persons_to_create)

    for person in persons_to_create:
        for skill in set(random.choices(skills_to_create, k=3)):
            person.skills.add(skill)

        person.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=64, unique=True, verbose_name="Stanowisko"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=64, unique=True, verbose_name="Imię"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Persons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=64, verbose_name="Imię")),
                ("last_name", models.CharField(max_length=64, verbose_name="Nazwisko")),
                (
                    "position",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="persons.position",
                        verbose_name="Stanowisko",
                    ),
                ),
                (
                    "skills",
                    models.ManyToManyField(
                        to="persons.skills", verbose_name="Umiejętności"
                    ),
                ),
            ],
        ),
        migrations.RunPython(fill_models_with_data, migrations.RunPython.noop),
    ]
