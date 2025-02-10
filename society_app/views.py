from django.shortcuts import render, redirect
from .forms import MemberForm

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
from django.shortcuts import render

def home(request):
    return render(request, "society_app/home.html")

