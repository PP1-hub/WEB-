from django.db import models

# Create your models here.
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="")
    city = models.CharField(max_length=300)
    address = models.TextField(default="")

    class Meta:
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.id}: name: {self.name}, city: {self.city}'

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="")
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.id}: name: {self.name}, salary: {self.salary}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': {
                'id': self.company.id,
                'name': self.company.name
            },
        }