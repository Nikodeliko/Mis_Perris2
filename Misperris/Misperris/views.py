from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import AgregarUsuario, Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario

def plantilla_cargada(request):
	return render_to_response("index.html")

acciones=[
   {'Mostrar':'Home','url':'inicio'}
]
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('gestionarUsuarios')
    else:
        return redirect('login')

def salir(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        usuario=Usuario(user=regDB,perfil=data.get("perfil"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    return render(request,"GestionarUsuarios.html",{'actual':actual,'form':form,'usuarios':usuarios,'acciones':acciones,})

'''
@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        regDB.save()
    usuarios=User.objects.all()
    form=AgregarUsuario()
    return render(request,"GestionarUsuarios.html",{'actual':actual,'form':form,'usuarios':usuarios,})
'''
def ingresar(request):
    form=Login(request.POST or None)
    if form.is_va
        data=form.cleaned_datalid():
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('gestionarUsuarios')
    return render(request,"login.html",{'form':form,})

def agregarusuario(request):
    if form.is_valid():
        data=form.cleaned_data
       # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        usuario=Usuario(user=regDB,perfil=data.get("perfil"))
        regDB.save()
        usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    return render(request,"agregarusuario.html",{'actual':actual,'form':form,'usuarios':usuarios,'acciones':acciones,})

# Vista de cliente para adoptar un perrito  :3
def Vista_adopcion(request):
    return render_to_response("./Vista/Vista.html")
def Vista_adopcion2(request):
    return render_to_response("./Vista/Vista2.html")
def Vista_adopcion3(request):
    return render_to_response("./Vista/Vista3.html")
def Vista_adopcion4(request):
    return render_to_response("./Vista/Vista4.html")
