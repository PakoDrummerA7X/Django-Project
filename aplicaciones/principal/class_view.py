#VISTAS BASADAS EN CLASES
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView #VIEW
from .forms import PersonaForm
from .models import Persona

"""

class View(): 
    model = Persona
    template_name = 'index.html'

    def get_queryself(self):
        return self.model.objects.all()

    def get_templates_names():
        return self.template_name

    def get(self,request,*args,**kwargs):
        return render(request,self.get_templates_names(),self.get_queryself())
"""