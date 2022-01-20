from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Items



def recommend(request):
		products = Items.objects.all()
		context = {'products':products}
		return render(request, 'recommend.html', context)
