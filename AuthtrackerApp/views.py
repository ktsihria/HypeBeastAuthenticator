from django.shortcuts import render
from AuthtrackerApp.form import Barcode
# Create your views here.


def main_page(request):
    return render(request,'AuthTracker/main_page.html')

def form_barcode(request):

    return render(request, 'AuthTracker/response_page.html')
