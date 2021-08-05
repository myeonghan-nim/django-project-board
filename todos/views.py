from django.shortcuts import render, redirect

from .models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    Todo.objects.create(
        author=request.POST.get('author'),
        title=request.POST.get('title'),
        due_date=request.POST.get('due-date'),
        content=request.POST.get('content'),
    )
    return redirect('todos:index')


def add(request):
    if request.method == 'POST':
        Todo.objects.create(
            author=request.POST.get('author'),
            title=request.POST.get('title'),
            due_date=request.POST.get('due-date'),
            content=request.POST.get('content'),
        )
        return redirect('todos:index')
    else:
        return render(request, 'add.html')


def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('todos:index')


def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.author = request.POST.get('author')
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due-date')
        todo.content = request.POST.get('content')
        todo.save()
        return redirect('todos:index')
    else:
        context = {
            'todo': todo,
        }
        return render(request, 'update.html', context)
