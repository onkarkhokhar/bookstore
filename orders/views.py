from django.views.generic.base import TemplateView
from django.conf import settings

from django.shortcuts import render

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context
