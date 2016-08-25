from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, View

from .models import *


class HomeView(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        c = super(HomeView, self).get_context_data(**kwargs)
        c['products'] = Product.objects.all()
        return c


class BillView(View):
    template_name = 'store/bill.html'

    def get(self, request):
        if not request.session.get('bill'):
            request.session['bill'] = []
        context = {'bill': [(Product.objects.get(id=code), qty)
            for code, qty in request.session.get('bill')]}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.POST.get('reset_bill'):
            request.session['bill'] = []
            context = {'bill': [(Product.objects.get(id=code), qty)
                for code, qty in request.session.get('bill')]}
            return render(request, self.template_name, context)

        elif request.POST.get('product_code'):
            product_code = request.POST.get('product_code')
            quantity = request.POST.get('quantity')

            if not request.session.get('bill'):
                request.session['bill'] = []

            request.session['bill'].append((product_code, quantity))
            request.session.modified = True

            context = {'bill': [(Product.objects.get(id=code), qty)
                for code, qty in request.session.get('bill')]}
            return render(request, self.template_name, context)

        elif request.POST.get('commit'):
            bill = Bill.objects.create()
            for code, qty in request.session.get('bill'):
                product = Product.objects.get(id=code)
                ProductSale.objects.create(product=product, bill=bill, quantity=qty)
            request.session['bill'] = []
            return redirect('/')
