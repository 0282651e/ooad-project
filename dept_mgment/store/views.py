from django.shortcuts import render

# Create your views here.
def show_bill_form(request):
	return render(request,'store/bill_form.html')
# def ProductSearch(request):
	