from django.shortcuts import render,redirect
from .models import Todos

def index(request):
    ob = Todos.objects.all()[:10]
    return render(request,'todos/index.html',{'ob':ob})

def detail(request,todo_id):
    todo =  Todos.objects.get(id=todo_id)
    return render(request,'todos/detail.html',{'todo':todo})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        todo = Todos(title=title,text=text)
        todo.save()
        return redirect('/')
    else:
        return render(request,'todos/add.html')
