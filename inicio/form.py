from django import forms

class PerroForularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    
class CrearPerroFormulario(PerroForularioBase):
    ...
    
class ModificarPerroFormulario(PerroForularioBase):
    ...

class BuscarPerroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)