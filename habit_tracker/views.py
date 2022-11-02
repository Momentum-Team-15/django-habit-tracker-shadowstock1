from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'habit_tracker/index.html')

