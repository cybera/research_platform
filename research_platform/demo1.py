import sys
import time
import select
import paramiko
import socket
import os

host = '208.75.74.96'

#
# Try to connect to the host.
# Retry a few times if it fails.
#
def main(command):
	i =1
	while True:
		try:
			paramiko.util.log_to_file("support_scripts.log")
			ssh = paramiko.SSHClient()
#			privatekeyfile = os.path.expanduser('/home/ubuntu/research_platform/research_platform/rsp-dev.pem')
			privatekeyfile = os.path.expanduser('~/research_platform/research_platform/rsp-dev.pem')
			mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.load_system_host_keys()
			ssh.connect(host, port=22, username='ubuntu',password='', pkey=mykey)
			break
		except paramiko.AuthenticationException:
			sys.exit(1)
		except:
			i += 1
			time.sleep(2)
	if i == 30:
		sys.exit(1)

	sys.stdout = open('/home/ubuntu/research_platform/research_platform/static/log.txt', 'w')
	stdin, stdout, stderr = ssh.exec_command(command)

# Wait for the command to terminate
	while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
		if stdout.channel.recv_ready():
			rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
			if len(rl) > 0:
            # Print data from stdout
				data = stdout.channel.recv(1024)
				sys.stdout.write(data.decode("utf-8"))
				sys.stdout.flush()

#
# Disconnect from the host
#
#	print "Command done, closing SSH connection"
	ssh.close()

if __name__ == "__main__":
	main(sys.argv[1])
