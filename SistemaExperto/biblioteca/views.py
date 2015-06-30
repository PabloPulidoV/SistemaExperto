from django.shortcuts import render
from django.http import HttpResponse
from biblioteca.models import Imperativo
from biblioteca.models import Tipos
from biblioteca.models import Lenguajes


def formulario_buscar(request):
	return render(request,'formulario_buscar.html')

def Lenguaje_Imp(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True 
		else:
			impera = Imperativo.objects.filter(nombre__icontains=q)
			tiposs =Tipos.objects.filter(tipo1__icontains=q)
			return render(request, 'resultados.html', {'impera': impera, 'query': q, 'tiposs': tiposs})	
	return render(request,'formulario_buscar.html', {'error': True}) 

def estructurado(request):
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True 
		else:
			impera = Lenguajes.objects.filter(tipo__icontains=q)
			return render(request, 'estructurado.html', {'impera': impera, 'query': q})	
	return render(request,'formulario_buscar.html', {'error': True}) 	

		







		

##def buscar(request):
##	error = False
##	if 'q' in request.GET:
##		q = request.GET['q']
##		if not q:
##			error = True 
##		else:
##			libros = Libro.objects.filter(titulo__icontains=q)
##			return render(request, 'resultados.html', {'libros': libros, 'query': q})	
##	return render(request,'formulario_buscar.html', {'error': True}) 
