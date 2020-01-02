from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<h1>Hello World!</h1>")
#
# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
#
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")
#

# def products(request, productid=34):
#     output = "<h2>Product № {0}</h2>".format(productid)
#     return HttpResponse(output)
#
#
# def users(request, id, name):
#     output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
#     return HttpResponse(output)

# def index(request):
#     header = "Personal Data"  # обычная переменная
#     langs = ["English", "German", "Spanish"]  # массив
#     user = {"name": "Tom", "age": 23}  # словарь
#     addr = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": addr}
#     return render(request, "index.html", context=data)

from django.template.response import TemplateResponse
def index(request):
    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = {"name": "Niko", "age": 43}  # словарь
    addr = ("Мандариновая", 4, 433)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "index.html", data)


# def index(request):
# #     # return render(request, "index.html")
# #     return render(request, "firstapp/home.html")
#     data = {"header": "Hello Django 2.5.1", "message": "Welcome to Python"}
#     return render(request, "index.html", context=data)

# from django.template.response import TemplateResponse
# def index(request):
#     return TemplateResponse(request, "firstapp/home.html")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)

#==============================
from django.shortcuts import render
from .forms import UserForm, UserForm2, UserForm3, UserForm4

def index_form(request):
    # userForm = UserForm()
    userForm = UserForm(field_order=["age", "name"])
    return render(request, "index_form.html", {"form": userForm} )

def form2(request):
    # userForm = UserForm()
    userForm = UserForm2(field_order=["age", "name"])
    return render(request, "index_form.html", {"form": userForm} )

def form3(request):  # бывштй index
    userform = UserForm2
    if request.method == "POST":
        userform = UserForm2(request.POST) # Если приходит POST-запрос,
             # то в начале заполняем форму пришедшими данными:
        if userform.is_valid(): # Потом проверяем mих корректность:
            name = userform.cleaned_data["name"]
            # После проверки на валидность мы можем получить
            # данные через объект cleaned_data (если данные корректны):
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm2()
        return render(request, "index_form.html", {"form": userform})

def form33(request):  # бывштй index
    userform = UserForm3
    if request.method == "POST":
        userform = UserForm3(request.POST) # Если приходит POST-запрос,
             # то в начале заполняем форму пришедшими данными:
        if userform.is_valid(): # Потом проверяем mих корректность:
            name = userform.cleaned_data["name"]
            # После проверки на валидность мы можем получить
            # данные через объект cleaned_data (если данные корректны):
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))

    return render(request, "index_form3.html", {"form": userform})

def form4(request):  # бывштй index
    userform = UserForm4
    if request.method == "POST":
        userform = UserForm4(request.POST) # Если приходит POST-запрос,
             # то в начале заполняем форму пришедшими данными:
        if userform.is_valid(): # Потом проверяем mих корректность:
            name = userform.cleaned_data["name"]
            # После проверки на валидность мы можем получить
            # данные через объект cleaned_data (если данные корректны):
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))

    return render(request, "index_form3.html", {"form": userform})