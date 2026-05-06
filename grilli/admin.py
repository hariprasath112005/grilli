from django.contrib import admin
from .models import EmailModel, TableModel
# Register your models here.
admin.site.register(EmailModel)
admin.site.register(TableModel)