from django.shortcuts import render
from customer_portal.forms import CompanyForm, ClientForm, TicketForm, ClientSearchForm
from customer_portal.models import Company, Client, Ticket
from django.shortcuts import redirect


def home_view(request):
    return render(request, "customer_portal/home.html")

# COMPANY
def list_company_view(request):
    companies = Company.objects.all()
    contexto_dict = {"companies": companies}
    return render(request, "customer_portal/list_company.html", contexto_dict)


def create_company_with_form_view(request):
    if request.method == "GET":
        contexto = {"form": CompanyForm()}
        return render(request, "customer_portal/form_company.html", contexto)
    elif request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            email_domain = form.cleaned_data['email_domain']
            company = Company(company_name=company_name, email_domain=email_domain)
            company.save()
            return redirect("company-detail", company_id=company.id)
        contexto = {"form": form}
        return render(request, "customer_portal/form_company.html", contexto)


def detail_company_view(request, company_id):
    company = Company.objects.get(id=company_id)
    contexto_dict = {"company": company}
    return render(request, "customer_portal/detail_company.html", contexto_dict)
# COMPANY

# CLIENT
def list_client_view(request):
    clients = Client.objects.all()
    contexto_dict = {"clients": clients}
    return render(request, "customer_portal/list_client.html", contexto_dict)


def create_client_with_form_view(request):
    if request.method == "GET":
        contexto = {"form": ClientForm()}
        return render(request, "customer_portal/form_client.html", contexto)
    elif request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            client = Client(first_name=first_name, last_name=last_name, email=email, company=company)
            client.save()
            return redirect("client-detail", client_id=client.id)
        contexto = {"form": form}
        return render(request, "customer_portal/form_client.html", contexto)


def detail_client_view(request, client_id):
    client = Client.objects.get(id=client_id)
    contexto_dict = {"client": client}
    return render(request, "customer_portal/detail_client.html", contexto_dict)
# CLIENT

# TICKET
def list_ticket_view(request):
    tickets = Ticket.objects.all()
    contexto_dict = {"tickets": tickets}
    return render(request, "customer_portal/list_ticket.html", contexto_dict)


def create_ticket_with_form_view(request):
    if request.method == "GET":
        contexto = {"form": TicketForm()}
        return render(request, "customer_portal/form_ticket.html", contexto)
    elif request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_name = form.cleaned_data['ticket_name']
            description = form.cleaned_data['description']
            due_date = form.cleaned_data['due_date']
            client = form.cleaned_data['client']
            ticket = Ticket(ticket_name=ticket_name, description=description, due_date=due_date, client=client)
            ticket.save()
            return redirect("ticket-detail", ticket_id=ticket.id)
        contexto = {"form": form}
        return render(request, "customer_portal/list_ticket.html", contexto)


def detail_ticket_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    contexto_dict = {"ticket": ticket}
    return render(request, "customer_portal/detail_ticket.html", contexto_dict)

def search_ticket_view(request):
    if request.method == "GET":
        form = ClientSearchForm()
        return render(request, "customer_portal/form_search.html", context={"form": form})
    elif request.method == "POST":
        form = ClientSearchForm(request.POST)
        tickets = []
        if form.is_valid():
            email = form.cleaned_data['email']
            tickets = Ticket.objects.filter(client__email__contains=email).all()
        contexto_dict = {"tickets": tickets}
        return render(request, "customer_portal/list_ticket.html", contexto_dict)
# TICKET