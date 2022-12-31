from django.http import HttpResponse


class StripWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):