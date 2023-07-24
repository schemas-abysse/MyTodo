from django.http import HttpResponse
from django.shortcuts import render

from .models import TodoList


def todo_list(request):
    todos = TodoList.objects.all()
    return render(request, "pages/todo_list.html", context={"todos": todos})


# def todo_list(request):
#     todos = TodoList.objects.order_by('todo_title')
#     return render(request, 'modules/todo_list/index.html', context={"todos": todos})


def add_todo(request):
    TodoList.objects.get_or_create(
        todo_title=request.POST['todo_title'],
        todo_level=request.POST['todo_level']
    )
    todos = TodoList.objects.order_by('todo_created')
    return render(request, 'components/todo_elements.html', context={"todos": todos})


def del_todo(request, pk):
    todo_to_delete = TodoList.objects.get(pk=pk)
    todo_to_delete.delete()
    return HttpResponse(f'')