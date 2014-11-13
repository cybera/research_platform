from django.http import HttpResponse
from django.shortcuts import render

def run(request):
	if request.method == "GET":
		return render(request, 'run.html')
	elif request.method == 'POST':
		response = request.POST.get('value')
		return HttpResponse(response)	
