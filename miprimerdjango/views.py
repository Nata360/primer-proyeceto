from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro

# v1
# def inicio(request):
#     return HttpResponse('Hola, soy el nuevo inicio')
#v2
# def inicio(request):
#     archivo = open(r'C:\Programación\mi_primer_django\templates\inicio.html')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Acá está el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25))
#     }

#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)

#v3

def inicio(request):
    # archivo = open(r'C:\Programación\mi_primer_django\templates\inicio.html')
    # template = Template(archivo.read())
    # archivo.close()
    
    template = loader.get_template('inicio.html')
    
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Acá está el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25))
    }
    # contexto = Context(diccionario)
    # renderizar_template = template.render(contexto)
    
    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)

def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista</h1>')

def fecha_actual(request):
    
    fecha = datetime.now()
    
    return HttpResponse(f'<h1>Fecha actual: {fecha}</h1>')

def saludar(request):
    return HttpResponse('Bienvenudo/a!!')

def bienvenudo(request, nombre, apellido):
    return HttpResponse(f'Bienvenudo/a {nombre.title()} {apellido.title()}!!')

def crear_perro(request, nombre, edad):
     
    template = loader.get_template('crear_perro.html')
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
       'perro': perro
    }

    renderizar_template = template.render(diccionario)
    return HttpResponse(renderizar_template)

