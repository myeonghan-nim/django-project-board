from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):

    todos = Todo.objects.all()

    context = {
        'todos': todos,
    }

    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):

    author = request.POST.get('author')
    title = request.POST.get('title')
    due_date = request.POST.get('due-date')
    content = request.POST.get('content')

    todo = Todo.objects.create(
        author=author,
        title=title,
        due_date=due_date,
        content=content
        )

    return redirect('todos:index')


# if you want make new and create logic at once, write add logic like this
def add(request):

    if request.method == 'POST':
        author = request.POST.get('author')
        title = request.POST.get('title')
        due_date = request.POST.get('due-date')
        content = request.POST.get('content')

        todo = Todo.objects.create(
            author=author,
            title=title,
            due_date=due_date,
            content=content
            )

        return redirect('todos:index')
    else:
        return render(request, 'add.html')


def delete(request, id):

    todo = Todo.objects.get(id=id)
    todo.delete()

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
        