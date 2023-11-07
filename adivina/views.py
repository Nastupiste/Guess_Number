from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'adivina/home.html')


def guess(request):
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(request.POST['guess'])

    if numero_usuario == numero_aleatorio:
        mensaje = "¡Felicidades! ¡¡Has acertado el número correcto!!"
    elif numero_usuario > numero_aleatorio:
        mensaje = "El número que has introducido es mayor"
    elif numero_usuario < numero_aleatorio:
        mensaje = "El número que has introducido es menor"

    return render(request, 'adivina/guess.html', {'mensaje': mensaje})
