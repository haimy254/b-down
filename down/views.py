from .models import Profile
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from .forms import NewUserForm, PostForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages

# registration 
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request,"register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", context={"login_form":form})


def home(request):
    return render (request,"home.html")

#adding a single post
def add_post(request):
	if request.method == "POST":
		post_form= PostForm(request.POST)

		if post_form.is_valid():
			obj = post_form.save(commit = False)
			obj.user = request.user
			profile = Profile.object.get(user=request.user)
			obj.profile = profile

			obj.save()
			return render('post_detail')
		else:
			post_form = PostForm()
			context = {
        'post_form': post_form
    }
	return render(request,'post_detail.html',{})

