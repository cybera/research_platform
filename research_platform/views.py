from django.http import HttpResponse
from django.shortcuts import render
from research_platform import demo1
from django import forms

class commandform(forms.Form):
        runcommand = forms.CharField(label='Run this Command: ',max_length=100)

def runcommand(request):
	if request.method == 'POST':
		httpresp = HttpResponse()
		form = 	commandform(request.POST)
		if form.is_valid():
			command_to_run = form.cleaned_data['runcommand']
			if command_to_run == "meme":
				with open("/home/ubuntu/research_platform/research_platform/static/testing.jpeg", "rb") as f:
					httpresp = HttpResponse(f.read(), content_type="image/jpeg")
			else:
				demo1.main(command_to_run)
				with open("/home/ubuntu/research_platform/research_platform/static/log.txt", "rb") as f:
					httpresp = HttpResponse(f.read(), content_type="text/plain")
		return httpresp
	else:
		form = commandform()
	return render(request, 'runcommand.html', {'form':form})
