from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from usuario.form import MiFormularioDeCreacionDeUsuarios, MiFormularioDeEdicionDeDatosDeUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuario.models import InfoExtra


# Create your views here.


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user) # esto hace que al terminar de loguear revisa si tiene infoextra relacionado, si existe lo trae, si no lo crea
            
            return redirect('Inicio:inicio')
        else:
            return render(request, ',usuario/login.html', {'formulario': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})

def registrarse(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Inicio:inicio')
        else: 
            return render(request, 'usuario/registro.html', {'formulario': formulario})
    formulario = MiFormularioDeCreacionDeUsuarios
    return render(request, 'usuario/registro.html', {'formulario': formulario})

@login_required  
def editar_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            
            formulario.save()
            return redirect('Inicio:inicio')
    else:   #minuto 0:43:00 hay alternativa de esto
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(initial={'avatar': info_extra_user.avatar}, instance=request.user)
        
    return render(request, 'usuario/editar_perfil.html', {'formulario': formulario})

class ModificarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/modificar_password.html'
    success_url = reverse_lazy('usuario:modificar_pass')
    