from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MemberForm

def home(request):
    return HttpResponse("Welcome to Milan Society Web App!")

def register_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect after successful registration
    else:
        form = MemberForm()

    return render(request, "society_app/register.html", {"form": form})

def success_page(request):
    return render(request, "society_app/success.html")

def home(request):
    return render(request, "society_app/home.html")
