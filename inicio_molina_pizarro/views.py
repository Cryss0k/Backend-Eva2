from django.shortcuts import render

def inicio(request):
    contexto = {
        'temas': [
            {'id': 1, 'nombre': 'Desarrollo Backend', 'descripcion': 'Todo sobre Django y Python.'},
            {'id': 2, 'nombre': 'Ciberseguridad', 'descripcion': 'Protección de sistemas y redes.'}
        ]
    }
    return render(request, 'inicio.html', contexto)

def detalle_tema(request, tema_id):
    return render(request, 'detalle.html', {'tema_id': tema_id})