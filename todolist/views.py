from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import todo

@login_required
def home_view(request):
  if request.method == "POST":
    task_name = request.POST.get("task_name")

    new_task = todo(user=request.user, task_name=task_name)
    new_task.save()

  all_tasks = todo.objects.filter(user=request.user)
  context = {
    "tasks" : all_tasks
  }

  return render(request,"home.html", context)

def login_page_view(request):
  if request.user.is_authenticated:
    return redirect("home")
  if request.method == "POST": 
    username = request.POST.get("username")
    password = request.POST.get("password")

    validate_user = authenticate(username=username, password=password)
    if validate_user is not None:
      login(request, validate_user)
      return redirect("home")
    else:
      messages.error(request, "User Does'nt Exist, Or Wrong Data")
      return redirect('login')

  return render(request, "login.html")

def logout_view(request):
  logout(request)
  return redirect("login")

def register_view(request):
  if request.user.is_authenticated:
    return redirect("home")
  if request.method == "POST":
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    password_again = request.POST.get("password_again")

    # Check if password less than required
    if len(password) < 8:
      messages.error(request, "Your Password Is Two Short")
      return redirect('register')
    # Check If Two Passwords are equal
    if password != password_again:
      messages.error(request, "Passwords dont't match")
      return redirect('register')
    # Check if user name is already exists
    get_users_names = User.objects.filter(username=username)
    if get_users_names:
      messages.error(request, "Username Is Already Exists")
      return redirect('register')

    new_user = User.objects.create_user(username=username, email=email, password=password)
    messages.success(request, "User Successfully Created")
    return redirect("login")
    # new_user.save()
  return render(request, "create_user.html")

@login_required
def delete_task(request, name):
  get_todo = todo.objects.get(user=request.user, task_name=name)
  get_todo.delete()
  return redirect("home")

@login_required
def update_task(request, name): 
  get_todo = todo.objects.get(user=request.user, task_name=name)
  get_todo.status =  not get_todo.status
  get_todo.save()
  return redirect("home")