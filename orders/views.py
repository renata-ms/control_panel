# Create your views here.

from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from orders.models import Order, Customer

import sys


class CustomersList(ListView):
    model = Order


class CustomerDetails(DetailView):
    model = Customer
