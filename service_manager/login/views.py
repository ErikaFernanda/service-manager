from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, viewsets
from django.contrib.auth.views import LoginView
from home.models import Company
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from login.serializers import IsValidTokenSerializer, LoginSerializer, RefreshSerializer
from django.http import JsonResponse
from login.backends import CustomBackend
from rest_framework.decorators import action
from login.utils import generate_jwt
from rest_framework.response import Response
from home.serializers import CompanySerializer


# class RefreshViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=["post"])
#     def refresh(self, request):
#         serializer = RefreshSerializer(data=request.data)

#         if not serializer.is_valid():
#             return JsonResponse(serializer.errors)

#         user = SmartUser.objects.filter(id=request.access_token.get("user_id")).first()

#         if not user:
#             return Response({"error": "Invalid access token"})

#         decoded_jwt = validate_jwt(serializer.data["refresh_token"])

#         if decoded_jwt.get("user_id") != request.access_token.get("user_id"):
#             return Response({"error": "Invalid refresh token"})

#         access_token = generate_jwt(user, "access")
#         refresh_token = generate_jwt(user, "refresh")

#         return Response({"access_token": access_token, "refresh_token": refresh_token})

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors)
        username = serializer.data["username"]
        password = serializer.data["password"]
        company_id = serializer.data["company_id"]

        user = CustomBackend.authenticate(username, password, company_id)

        if not user:
            return JsonResponse({"error": "Invalid username or password"}, status=401)

        refresh_token = generate_jwt(user, company_id, "refresh")
        access_token = generate_jwt(user, company_id, "access")
        return Response({"access_token": access_token, "refresh_token": refresh_token})


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
