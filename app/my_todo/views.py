from django.http import HttpResponse
from django.shortcuts import render

from .models import TodoList


# Create your views here.
def todo_list(request):
    todos = TodoList.objects.order_by('todo_title')

    return render(request, 'modules/todo_list/index.html', context={"todos": todos})


def add_todo(request):
    TodoList.objects.create(
        todo_title=request.POST['title'],
    )
    return HttpResponse(f'<li class="list-group-item d-flex justify-content-between align-items-center">'
                        f'{request.POST["title"]}'
                        f'</li>')



def del_todo(request, pk):
    todo_to_delete = TodoList.objects.get(pk=pk)
    todo_to_delete.delete()
    return HttpResponse(f'')