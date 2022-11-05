from django.shortcuts import render, redirect
from .models import User, Habit, DailyRecord
from .forms import HabitForm

def index(request):
    habits = Habit.objects.all()
    return render(request, 'habit_tracker/index.html', {'habits':habits})

def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid:
            habit = form.save()
            habit.user = request.user
            habit.save()
            return redirect('home')
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/edit_habit.html', {'form': form})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habit_tracker/habit_detail.html', {'habit':habit})

def create_record(request, habitpk):
    dates = Date.objects.all()
    habit = Habit.objects.get(pk=habitpk)
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid:
            habit = form.save()
            habit.user = request.user
            habit.save()
            return redirect('home')
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/edit_habit.html', {'form': form})