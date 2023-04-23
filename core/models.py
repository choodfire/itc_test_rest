from django.db import models


class Address(models.Model):
    city = models.CharField(
        "Город",
        max_length=255,
    )
    street = models.CharField(
        "Улица",
        max_length=255,
    )
    house = models.IntegerField(
        "Номер дома",
    )


class University(models.Model):
    title = models.CharField(
        "Название",
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
    )


class Department(models.Model):
    title = models.CharField(
        "Название",
        max_length=255,
    )
    employees_number = models.IntegerField(
        "Количество сотрудников",
    )


class Lecturer(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(
        "Имя",
        max_length=255,
    )
    middle_name = models.CharField(
        "Фамилия",
        max_length=255,
    )
    last_name = models.CharField(
        "Отчество",
        max_length=255,
    )
    birth_year = models.IntegerField(
        "Год рождения",
    )
