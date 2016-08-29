from django.shortcuts import redirect, render
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
        # request.session['bill'] = []
        if not request.session.get('bill'):
            request.session['bill'] = []
        c = {}
        c['bill'] = [(Product.objects.get(id=code), int(qty),rate,total)
                     for code, qty, rate, total in request.session.get('bill')]
        # calculate grand total
        c['grand_total'] = 0
        for p, q, m, n in c['bill']:
            c['grand_total'] += n
        return render(request, self.template_name, c)

    def post(self, request):
        if request.POST.get('reset_bill'):
            request.session['bill'] = []

        elif request.POST.get('add'):
            product_code = request.POST.get('product_code')
            quantity = request.POST.get('quantity')
            rate = Product.objects.get(id=product_code).sell_price
            total = int(quantity)*rate
            if not request.session.get('bill'):
                request.session['bill'] = []

            request.session['bill'].append((product_code, int(quantity),rate,total))
            request.session.modified = True

        elif request.POST.get('commit'):
            # Check for stock
            for code, qty, rate, total in request.session.get('bill'):
                product = Product.objects.get(id=code)
                if product.stock < int(qty):
                    raise Exception("quantity is greater than stock")
            bill = Bill.objects.create()
            for code, qty, rate, total in request.session.get('bill'):
                product = Product.objects.get(id=code)
                product.stock -= int(qty)
                product.save()
                ProductSale.objects.create(product=product, bill=bill, quantity=qty, rate=rate, total=total)
            request.session['bill'] = []
        return redirect('store_bill')

class OrderView(View):
    template_name='store/order.html'

    def get(self,request):
        order = Order.objects.all()
        context = {'order':order}
        return render(request,self.template_name,context)


    def post(self, request):
       
        # Order Part
        if request.POST.get('order_button'):
            product_code = request.POST.get('order_product_code')
            quantity = request.POST.get('order_quantity')
            product = Product.objects.get(id=product_code)
            status = Status.objects.get(id=1)
            order = Order.objects.create(product=product,quantity_ordered=quantity,status=status)

        # Delivery Part
        if request.POST.get('deliver_button'):
            order_id = request.POST.get('delivery_id')
            quantity = request.POST.get('delivery_quantity')
            cost_price = request.POST.get('delivery_cost_price')
            sell_price = request.POST.get('delivery_sell_price')

            order = Order.objects.get(id=order_id)
            product =Product.objects.get(name=order.product)
            # if quantity<order.quantity_ordered:
            #     display warning msg
            product.stock+=int(quantity)
            product.cost_price=float(cost_price)
            product.sell_price=float(sell_price)
            product.save()
            order.status=Status.objects.get(id=2)
            order.save()
        return redirect('store_order')

        
class SupplierView(TemplateView):
    template_name='store/supplier.html'
    
    def get_context_data(self, **kwargs):
        c = super(SupplierView, self).get_context_data(**kwargs)
        c['supplier'] = Supplier.objects.all()
        return c


