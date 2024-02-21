from django.urls import path
from .views import *


urlpatterns = [
    path('invoice/',invoice_list,name='invoice'),
    path('invoice/<int:pk>',edit_invoice,name='edit-invoice'),

    path('invoice-details/',invoice_details_list,name='invoice-detials'),
    path('invoice-details/<int:pk>',edit_invoice_details,name='edit-invoice-detials'),
]
