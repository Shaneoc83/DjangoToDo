from django.shortcuts import render, HttpResponse
from todo.models import ToDoItem

# Create your views here.

def get_index_homepage_thingy(request):
    active_items = []

    if request.user.is_authenticated():
        active_items = ToDoItem.objects.filter(done=False, owner=request.user)

    return render(request, 'index.html', {'the_data': active_items})


def log_me_in(request):
    return render(request, 'profile.html')

