from django.conf.urls import url
from AuthtrackerApp import views

urlpatterns = [
    url('',views.form_barcode,name='barcode'),
    ]
