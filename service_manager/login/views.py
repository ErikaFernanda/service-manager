from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request, request.POST)
        # if form.is_valid():
        #     print("sssasasas")
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     user = authenticate(username=username, password=password)
        #     print("aaaa")
        #     if user is not None:
        #         login(request, user)
        return redirect('home')  # Substitua 'pagina_inicial' pelo nome da sua view inicial
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})