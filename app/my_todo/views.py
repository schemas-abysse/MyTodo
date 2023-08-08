from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET

from .models import TodoList


def todo_list(request):
    """
    This view returns all the elements of the list.
    Parameters:
        request (WSGIRequest): Request object
    Returns:
        HttpResponse: The 'todo_list' page
    """
    todos = TodoList.objects.all()
    return render(request, "pages/todo_list.html", context={"todos": todos})


def add_todo(request):
    """
    This view add a new element and returns the updated list
    Parameters:
        request (WSGIRequest): Request object
    Returns:
        HttpResponse: The 'todo_elements' HTML component charged with context datas
    """
    TodoList.objects.get_or_create(
        todo_title=request.POST['todo_title'],
        todo_level=request.POST['todo_level']
    )
    todos = TodoList.objects.order_by('todo_created')
    return render(request, 'components/todo_elements.html', context={"todos": todos})


@require_GET
def swap_element_title(request):
    return HttpResponse(f"<div class='col-10'>"
                        f"<input type='text' name='new_todo_title' class='form-control input-dark'>"
                        f"</div>"
                        f"<div class='col-1'>"
                        f"<button class='btn validate-button col-12'>"
                        f"<i class='bi bi-check2-circle'></i>"
                        f"</button>"
                        f"</div>"
                        f"<div class='col-1'>"
                        f"<button class='btn dismiss-button col-12' onclick='location.reload();'>"
                        f"<i class='bi bi-x-circle'></i>"
                        f"</button>"
                        f"</div>")


@require_POST
def update_todo(request, pk):
    """
    This view update an element of the list and return the updated list
    Parameters:
        request (WSGIRequest): Request object
        pk (int): Primary Key of the element
    Returns:
        HttpResponse: The 'todo_elements' HTML component charged with context datas
    """
    todo_to_update = TodoList.objects.get(pk=pk)
    if request.POST['new_todo_title'] is not None and request.POST['new_todo_title'] != todo_to_update:
        todo_to_update.todo_title = request.POST['new_todo_title']
    todos = TodoList.objects.order_by('todo_created')
    return render(request, 'components/todo_elements.html', context={"todos": todos})


def del_todo(request, pk):
    """
    This view deletes an element of the list and returns the updated list
    Parameters:
        request (WSGIRequest): Request object
        pk (int): Primary key of the element
    Returns:
        HttpResponse: The 'todo_elements' HTML component charged with context datas
    """
    todo_to_delete = TodoList.objects.get(pk=pk)
    todo_to_delete.delete()
    todos = TodoList.objects.order_by('todo_created')
    return render(request, 'components/todo_elements.html', context={"todos": todos})
