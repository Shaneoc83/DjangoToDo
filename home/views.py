from django.shortcuts import render, HttpResponse
from todo.models import ToDoItem

# Create your views here.

def get_index_homepage_thingy(request):
    active_items = ToDoItem.objects.filter(done=False)
    return render(request, 'index.html', {'the_data': active_items})


def log_me_in(request):
    return render(request, 'profile.html')

