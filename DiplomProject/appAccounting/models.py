from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class AccountInfo(models.Model):
    username = models.CharField("Имя пользователя", max_length=20)
    password = models.CharField("Пароль", max_length=20)
    user_budget = models.IntegerField("Бюджет")
    
    def __str__(self):
        return self.username

class ExpenseInfo(models.Model):
    expense_name = models.CharField("Название расходов", max_length=20)
    cost = models.FloatField("Расходы")
    date_added = models.DateField("Дата произведения расходов")
    user_expense = models.ForeignKey(User, verbose_name = "Расходы пользователя", on_delete=models.CASCADE)