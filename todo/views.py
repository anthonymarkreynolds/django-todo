from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    else:
        form = TodoForm
    return render(request, 'todo/create.html', {'form': form})


def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/update.html', {'form': form, 'todo': todo})


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:list')
    return render(request, 'todo/delete.html', {'todo': todo})
