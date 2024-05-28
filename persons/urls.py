from django.urls import path

from persons.views import SkillList, main, persons


app_name = "persons"
urlpatterns = [
    path("", main, name="main"),
    path("skills/", SkillList.as_view(), name="skills"),
    path("persons/", persons, name="persons"),
]
