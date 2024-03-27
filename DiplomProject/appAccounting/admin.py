from django.contrib import admin
from .models import AccountInfo, ExpenseInfo

@admin.register(AccountInfo)
class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'user_budget']
    list_display_links = ['username', 'user_budget']
    list_filter = ['username']
    list_per_page = 20

@admin.register(ExpenseInfo)
class ExpenseInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'expense_name', 'cost', 'date_added', 'user_expense']
    list_display_links = ['expense_name', 'cost', 'date_added', 'user_expense']
    list_filter = ['expense_name']
    list_per_page = 20