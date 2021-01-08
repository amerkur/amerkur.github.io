from django.http import request
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

task_list = [] 

# Create your views here.

class NewTaskForm(forms.Form):
    add_task = forms.CharField(label="Add Task")
    add_priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    return render(request, "tasks/index.html", {
        "todos": task_list
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form_add_task = form.cleaned_data["add_task"]
            form_add_priority = form.cleaned_data["add_priority"]
            task_list.append({'task': form_add_task, 'num': form_add_priority})
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })

    # If used GET instead of POST or first load of add.html
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })