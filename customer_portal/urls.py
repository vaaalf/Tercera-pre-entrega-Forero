from django.urls import path

from customer_portal import views

urlpatterns = [
    path("", views.home_view, name="home"),
    # COMPANY
    path("company/", views.list_company_view, name="company-list"),
    path("company/create/", views.create_company_with_form_view, name="company-create"),
    path("company/detail/<company_id>", views.detail_company_view, name="company-detail"),
    # COMPANY
    # CLIENT
    path("client/", views.list_client_view, name="client-list"),
    path("client/create/", views.create_client_with_form_view, name="client-create"),
    path("client/detail/<client_id>", views.detail_client_view, name="client-detail"),
    # CLIENT
    # TICKET
    path("ticket/", views.list_ticket_view, name="ticket-list"),
    path("ticket/create/", views.create_ticket_with_form_view, name="ticket-create"),
    path("ticket/detail/<ticket_id>", views.detail_ticket_view, name="ticket-detail"),
    path("ticket/find/", views.search_ticket_view, name="ticket-finder"),
    # TICKET
]