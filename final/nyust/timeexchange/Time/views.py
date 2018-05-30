from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Member,Seller
def index(request):
	return HttpResponse("hi")