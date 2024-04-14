from django import forms

from customer_portal.models import Company, Client, Ticket


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'email_domain']
        labels = {
            'company_name': 'Please register your company name',
            'email_domain': 'What is your domain?',
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', "email", "company"]
        labels = {
            'first_name': 'Your first name',
            'last_name': 'Your last name',
            'email': 'Your email',
            'company': 'Select your company',
        }

class ClientSearchForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, label="Your client's email")


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_name', 'description', "due_date", "client"]
        labels = {
            'ticket_name': 'Your request',
            'description': 'Describe your request',
            'due_date': 'Due date',
            'client': 'Which client are you?',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }