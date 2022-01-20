from django.shortcuts import render,redirect

def recipe(request):
	if request.user.is_authenticated:
		return render(request,"recipe.html")
	else:
		return redirect("user_login")
