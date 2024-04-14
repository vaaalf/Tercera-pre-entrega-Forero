from django.contrib import admin
from customer_portal import models

# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Client)
admin.site.register(models.Ticket)