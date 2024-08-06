from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Resume
from django.http import HttpResponse
from .forms.resume_form import ResumeForm


# Create your views here.
def index(req):
    if req.method == "POST":
        form = ResumeForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect("resume:index")
        else:
            return render(req, "resumes/new.html", {"form": form})

    items = Resume.objects.all()
    return render(req, "resumes/index.html", {"items": items})


def show(req, id):
    item = get_object_or_404(Resume, pk=id)
    form = ResumeForm(req.POST, instance=item)

    if req.method == "POST":
        form = ResumeForm(req.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect("resume:show", item.id)
        else:
            return render(req, "resumes/edit.html", {"form": form, "item": item})

    return render(req, "resumes/show.html", {"form": form, "item": item})


def new(req):
    form = ResumeForm()
    return render(req, "resumes/new.html", {"form": form})


def edit(req, id):
    item = get_object_or_404(Resume, pk=id)
    form = ResumeForm(instance=item)
    return render(req, "resumes/edit.html", {"form": form, "item": item})


def delete(req, id):
    item = get_object_or_404(Resume, pk=id)
    item.delete()
    return redirect("resume:index")
