import os
import sys
import time
from novaclient.v1_1 import client
from credentials import get_nova_creds
from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/home/ubuntu/research_platform/research_platform/research_platform/general.ini')

create_log = config.get('createvm', 'CREATE_LOG')
new_ip = config.get('createvm', 'NEW_IP')

def main(vm_name):
	sys.stdout = open(create_log, 'w')
	creds = get_nova_creds()
	novac = client.Client(**creds)
	image = novac.images.find(name="Ubuntu 14.04")
	flavor = novac.flavors.find(name="m1.small")
	instance = novac.servers.create(name=vm_name, image=image, flavor=flavor, key_name="rsp-dev")

# Poll at 5 second intervals, until the status is no longer 'BUILD'
	status = instance.status
	while status == 'BUILD':
		time.sleep(5)
		# Retrieve the instance again so the status field updates
		instance = novac.servers.get(instance.id)
		status = instance.status
	print("Your new instance is : %s" % status)

	if status == 'ACTIVE':
		instance = novac.servers.find(name=vm_name)
		instance.add_floating_ip(new_ip)
	print("IP Address for the instance is : %s",new_ip )
	sys.stdout.flush()
	sys.stdout.close()


if __name__ == "__main__":
	main(sys.argv[1])
