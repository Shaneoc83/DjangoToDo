from django import forms
from models import ToDoItem


class CreateToDoItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('description',)