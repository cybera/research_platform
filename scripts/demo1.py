import sys
import time
import select
import paramiko
import socket
import os

host = '208.75.74.96'
i = 1

#
# Try to connect to the host.
# Retry a few times if it fails.
#
while True:
    print "Trying to connect to %s (%i/30)" % (host, i)

    try:
        paramiko.util.log_to_file("support_scripts.log")
	ssh = paramiko.SSHClient()
        privatekeyfile = os.path.expanduser('/home/ubuntu/research_platform/research_platform/rsp-dev.pem')
	mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.load_system_host_keys()
	ssh.connect(host, port=22, username='ubuntu',password='', pkey=mykey)
        print "Connected to %s" % host
        break
    except paramiko.AuthenticationException:
        print "Authentication failed when connecting to %s" % host
        sys.exit(1)
    except paramiko.SSHException, e:
        print "Password is invalid:" , e
    except socket.error, e:
        print "Socket connection failed on %s:" % h, e
    except IOError, e:
	print "IOERROR", e
    except paramiko.PasswordRequiredException, e:
	print "password required", e
    except :
        print "Could not SSH to %s, waiting for it to start" % host
	i += 1
        time.sleep(2)

    # If we could not connect within time limit
    if i == 30:
        print "Could not connect to %s. Giving up" % host
        sys.exit(1)

# Send the command (non-blocking)
sys.stdout = open('/home/ubuntu/log.txt', 'w')
stdin, stdout, stderr = ssh.exec_command("ls -l")

# Wait for the command to terminate
while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        if len(rl) > 0:
            # Print data from stdout
            print stdout.channel.recv(1024),

#
# Disconnect from the host
#
print "Command done, closing SSH connection"
ssh.close()
