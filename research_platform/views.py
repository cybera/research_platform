from django.http import HttpResponse
from django.shortcuts import render
from research_platform import demo1
from research_platform import nova_createvm
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import sys
from research_platform import file_transfer
from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/home/ubuntu/research_platform/research_platform/research_platform/general.ini')
output_log = config.get('general','OUTPUT_FILE')
create_log = config.get('createvm', 'CREATE_LOG')
new_ip = config.get('createvm','NEW_IP')


class commandform(forms.Form):
        runcommand = forms.CharField(label='Run this Command: ',max_length=100)

class createvmform(forms.Form):
	createvm = forms.CharField(label='Spin up a vm', max_length=100)


class uploadfileform(forms.Form):
	file = forms.FileField(label='Choose a file to Upload:')

#This function gets the command that the user types in, then calls the main function in demo1.py to create a SSH session#
#with paramiko and runs the command on the newly created vm. The output of the command is then returned to the user's screen#

def runcommand(request):
        if request.method == 'POST':
                httpresp = HttpResponse()
                form =  commandform(request.POST)
                if form.is_valid():
                        command_to_run = form.cleaned_data['runcommand']
                        if command_to_run == "meme":
                                with open("/home/ubuntu/research_platform/research_platform/research_platform/static/testing.jpeg", "rb") as f:
                                        httpresp = HttpResponse(f.read(), content_type="image/jpeg")
                        else:
                                demo1.main(command_to_run)
                                with open(output_log, "rb") as f:
                                        httpresp = HttpResponse(f.read(), content_type="text/plain")
                return httpresp
        else:
                form = commandform()
        return render(request, 'runcommand.html', {'form':form})


#Like the name suggests, this function will create a vm instance at the location you want it to create it.#
#This funciton uses openstack nova client python api, you need set the nova creaentials in the nova_credentials.py#
#and also have the openrc file for your openstack cloud environment sourced and loaded#

def createvm(request):
	if request.method == 'POST':
		httpresp = HttpResponse()
                form =  createvmform(request.POST)
		if form.is_valid():
			vm_name = form.cleaned_data['createvm']
			nova_createvm.main(vm_name)
			with open(create_log ,"rb") as f:
                                        httpresp = HttpResponse(f.read(), content_type="text/plain")
		return httpresp
	else:
		form = createvmform()
	return render(request, 'createvm.html', {'form':form})

#writes the uploaded file to its destnation#

def handle_uploaded_file(file, filename):
    with open('/home/ubuntu/research_platform/research_platform/research_platform/static/%s'%filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

#This function helps in uploading a file or the user's script to their vm that was just created#

def upload_file(request):
	if request.method =='POST':
		form = uploadfileform(request.POST, request.FILES)
		if form.is_valid():
			file = request.FILES['file']
			file_name = file.name
			handle_uploaded_file(file, file_name)
			
			file_transfer.main(file_name,new_ip)	
			return HttpResponseRedirect('/success/')
	else:
		form = uploadfileform()
	return render(request, 'upload.html', {'form':form})

def success(request):
	return HttpResponse("Your file has been successfully uploaded")


