from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category
from .forms import *


def home(request):
    students = Category.objects.all()
    return render(request, "home.html", {"students": students})


def create_category(request):
    recipe_form = CategoryForm()
    return render(request, "create_category.html", {"form": recipe_form})


def save_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/recipe/')
        else:
            return render(request, 'create_category.html', {"form": form})

    else:
        form = CategoryForm()
        return render(request, 'create_category.html', {"form": form})


def AddImage(request, id):
    if request.method == 'POST':
        id = request.POST['id']
        category = Category.objects.get(id=id)
        image = Image(image=request.POST['img'], category=category)
        image.save()
        image = category.image_set.all()
        return render(request, 'add_image.html', {'categorys': category, 'images': image})
    else:
        category = Category.objects.get(id=id)
        image = category.image_set.all()
        return render(request, 'add_image.html', {'categorys': category, 'images': image})


def details(request, recipe_id):
    students = Category.objects.get(id=recipe_id)
    return render(request, "details.html", {"student": students})


def delete(request, recipe_id):
    Category.objects.get(id=recipe_id).delete()
    return HttpResponseRedirect('/recipe/')