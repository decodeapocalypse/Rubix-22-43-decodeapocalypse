from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Item
from recomapp.models import Items
import os
def home(request):
	if request.user.is_authenticated:
		return render(request,"home.html")
	else:
		return redirect("user_login")
	
def addProduct(request):
	if request.method == "POST":
		prod = Item()
		prod.name = request.POST.get('name')
		prod.date = request.POST.get('date')
		prod.price = request.POST.get('price')


		prodd=Items()
		prodd.name=request.POST.get('name')
		prodd.price=request.POST.get('price')
		
		if len(request.FILES) != 0:
			prod.image = request.FILES['image']

		prod.save()
		prodd.save()
		messages.success(request, "Product Added Successfully")
		return redirect('/')
	return render(request, 'add.html')

def index(request):
	products = Item.objects.all()
	context = {'products':products}
	return render(request, 'index.html', context)

def deleteProduct(request, pk):
	prod = Item.objects.get(id=pk)
	if len(prod.image) > 0:
		os.remove(prod.image.path)
	prod.delete()
	messages.success(request,"Product Deleted Successfuly")
	return redirect('/')

def ahome(request):
	return redirect('/')