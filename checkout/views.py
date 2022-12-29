from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForms


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment ")
        return redirect(revers('products'))

    order_form = OrderForms()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MK3JuCPvGNCIKNA4xArHVWlFFo4SLhBblQYe7BBWOboH0vUEMuf0DXmBXNQHfJ9hIrkzaVnhqXQolZ0HmguleP900HSbTDuhQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)