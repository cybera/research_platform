canarie-rsp
===========

This repository is for managing source code for CANARIE's - Research Software Platform

1. Go to url "your_host_name_or_public_ip/createvm" and provide a name for the vm instance that you want.
Then Click on createvm button, a vm instance will be created on your cloud. You need to source your openrc 
file and provide the cloud credentials in the credentials.py before trying to create a vm.
2. Then go to url "your_host_name_or_public_ip/upload_file", click on the browse to choose a file and click upload.
Once the file is uploaded to your new vm (created in the above step)  you will get a success message.
3. Finally you could go to url "your_host_name_or_public_ip/runcommand", then type in the command you need to run
and click runcommand button. The host will create an ssh session with the new vm using paramiko to run the command
and gets the response back to the screen.
