from .forms import addForm,RegForm,LoginForm
from django.shortcuts import render,get_object_or_404,redirect
from .models import fooddetail
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import login as auth_login,logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.urls import reverse 
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .utility import *
from django.db.models import Q

# Create your views here.
def post_recipe(request):
    detail = fooddetail.objects.all()
    return render(request,'foodrecipe/home.html',{'detail':detail})

def add_recipe(request):
    if request.method == "POST":
        form = addForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('food_detail', pk=obj.pk)
    return render(request,'foodrecipe/add_recipe.html',{})

def recipe_edit(request,pk):
    post = get_object_or_404(fooddetail, pk=pk)
    if request.method == "POST":
        form = addForm(request.POST or None, request.FILES or None,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('food_detail', pk=post.pk)
    else:
        form = addForm(instance=post)
    return render(request, 'foodrecipe/recipe_edit.html', {'form': form,'pk':pk})
   
def food_detail(request,pk):
    detail = get_object_or_404(fooddetail,pk=pk)
    return render(request,'foodrecipe/food_detail.html',{'detail':detail})

class RegFormview(View):

    def post(self,request):
        form = RegForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request=request, user=user)
                return HttpResponseRedirect(reverse('post_recipe'))
        msg_to_html = custom_message('Invalid Credentials', TagType.danger)
        dictionary = dict(request=request, messages = msg_to_html)
        dictionary.update(csrf(request))
        return render(request,'foodrecipe/base.html', dictionary)

  
def LoginFormview(request):
     if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request=request, user=user)
            return HttpResponseRedirect(reverse('post_recipe'))
        else:
            msg_to_html = custom_message('Invalid Credentials', TagType.danger)
            dictionary = dict(request=request, messages = msg_to_html)
            dictionary.update(csrf(request))
        return render(request,'foodrecipe/base.html', dictionary)
    
def Logout_view(request):
    logout(request)
    return redirect('post_recipe')

def search(request):
    if request.method=="POST":
        string = request.POST.get('str')
        if string:
            match = fooddetail.objects.filter(Q(name__icontains=string) | Q(ingredients__icontains=string))
            if match:
                return render(request,'foodrecipe/home.html',{'detail':match})
            else:
                msg_to_html = custom_message('No Result Found', TagType.danger)
                dictionary = dict(request=request, messages = msg_to_html)
                dictionary.update(csrf(request))
            return render(request,'foodrecipe/base.html', dictionary)

def my_recipe(request):
    detail = fooddetail.objects.filter(author=request.user)
    if detail:
        return render(request,'foodrecipe/my_recipe.html',{'detail':detail})
    else:
        msg_to_html = custom_message('No Recipes are Added', TagType.danger)
        dictionary = dict(request=request, messages = msg_to_html)
        dictionary.update(csrf(request))
        return render(request,'foodrecipe/my_recipe.html', dictionary)

def contact(request):
    return render(request,'foodrecipe/contact.html',{})
