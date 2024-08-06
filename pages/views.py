from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(req):
    return render(req, "pages/index.html")


def about(req):
    return render(req, "pages/about.html")
