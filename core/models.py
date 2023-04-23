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

    def __str__(self):
        return f'{self.city}, {self.street} {self.house}'


class University(models.Model):
    title = models.CharField(
        "Название",
        max_length=255,
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(
        "Название",
        max_length=255,
    )
    employees_number = models.IntegerField(
        "Количество сотрудников",
    )
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
    )

    def get_number(self):
        return f'Количество: {self.employees_number}'

    def __str__(self):
        return self.title


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

    def __str__(self):
        return f'{self.middle_name} {self.first_name} {self.last_name}'
