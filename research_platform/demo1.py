import sys
import time
import select
import paramiko
import socket
import os
from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/home/ubuntu/research_platform/research_platform/research_platform/general.ini')

host = config.get('general', 'HOST')
log_file = config.get('general', 'OUTPUT_FILE')
priv_key = config.get('general', 'PRIV_KEY')

#gets the command that the user wants to run, creates a SSH session with the user's vm using#
#paramiko util and runs the command their. The output of the command is then returned back to the user's screen`#
def main(command):
    paramiko.util.log_to_file("/home/ubuntu/research_platform/research_platform/research_platform/support_scripts.log")
    ssh = paramiko.SSHClient()
# privatekeyfile = os.path.expanduser('/home/ubuntu/research_platform/research_platform/rsp-dev.pem')
    privatekeyfile = os.path.expanduser(priv_key)
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port=22, username='ubuntu',password='', pkey=mykey)
    sys.stdout = open(log_file, 'w')
    stdin, stdout, stderr = ssh.exec_command(command)
    data = stdout.channel.recv(1024)
    sys.stdout.write(data.decode("utf-8"))
    sys.stdout.flush()
    ssh.close()

if __name__ == "__main__":
    main(sys.argv[1])
