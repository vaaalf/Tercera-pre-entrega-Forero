from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    email_domain = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.company_name} {self.email_domain}"


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email}) ({self.company})"


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    due_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self) -> str:
       return f"{self.ticket_name} {self.client}"