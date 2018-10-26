from django.shortcuts import render_to_response

# Create your views here.
def plantilla_cargada(request):
	return render_to_response("index.html")
