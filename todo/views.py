from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import CreateToDoItemForm

# Create your views here.
def new_todo_item(request):
    if request.method == "POST":
        form = CreateToDoItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CreateToDoItemForm()

    return render(request, 'new_todo.html', {'form': form})