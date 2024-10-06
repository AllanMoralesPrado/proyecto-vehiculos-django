from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from .forms import VehiculoForm

class AddVehicleView(View):
    form_class = VehiculoForm
    template_name = "add_vehiculo.html"
    title_page = "Añadir al Catálogo"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form, "title_page": self.title_page})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("agregar_vehiculo"))

        return render(request, self.template_name, {"form": form, "title_page": self.title_page})
