from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.views import LoginView
from home.models import Company
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder


def login_view(request, id_company):
    company = Company.objects.get(id=id_company)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['company_id'] = company.id
                request.session['company_name'] = company.name
                request.session['company_logo_url'] = company.logo_url

                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login/index.html', {'form': form, 'id_company': id_company, 'company': company})


def logout_view(request, id_company):
    logout(request)
    form = AuthenticationForm(request, request.POST)
    company = Company.objects.get(id=id_company)
    return render(request, 'login/index.html', {'form': form, 'id_company': id_company, 'company': company})


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
