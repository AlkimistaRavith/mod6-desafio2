from django.shortcuts import render


# Create your views here.
def empleados(request):
    lista_empleados = [
"Juan Mendez",
"Claudio Perez",
"Maria Rodriguez",
"Roberto Cordova",
"Pedro Abarca",
"Daniel Mejias"
    ]
    return render(request, "empleados.html", {"lista_empleados": lista_empleados})

