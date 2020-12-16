from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import model_to_dict
from hw21.forms import UserForm
from hw21.models import UserModel
from django.db.models.functions import Lower


def home(request):
    users = UserModel.objects.order_by(Lower('last_name')).all()
    context = {'users': users}
    return render(request, 'home.html', context)


def add_user(request):
    if request.method == "GET":
        context = {'form': UserForm()}
        return render(request, 'add_user.html', context)
    elif request.method == "POST":
        form = UserForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Your input is invalid', status=400)
        data = form.cleaned_data
        user = UserModel(**data)
        user.save()
        return redirect('home')


def detail_user(request, user_id):
    if request.method == "GET":
        user = UserModel.objects.filter(id=user_id).first()
        context = {'user': user}
        return render(request, 'detail_user.html', context)


def edit_user(request, user_id):
    if request.method == "GET":
        user = UserModel.objects.filter(id=user_id).first()
        context = {'form': UserForm(model_to_dict(user)), 'user': user}
        return render(request, 'edit_user.html', context)
    elif request.method == "POST":
        form = UserForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Your input is invalid', status=400)
        data = form.cleaned_data
        UserModel.objects.filter(id=user_id).update(**data)
        return redirect('home')


def delete_user(request, user_id):
    if request.method == 'POST':
        user = UserModel.objects.filter(id=user_id).first()
        user.delete()
        return redirect('home')
