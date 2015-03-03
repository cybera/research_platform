import sys
import time
import select
import paramiko
import socket
import os
from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/home/ubuntu/research_platform/research_platform/research_platform/general.ini')

transfer_log = config.get('filetransfer', 'TRANSFER_LOG')
priv_key = config.get('general', 'PRIV_KEY') 

def main(file_name, host):
    paramiko.util.log_to_file(transfer_log)
    ssh = paramiko.SSHClient()
    privatekeyfile = os.path.expanduser(priv_key)
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(host, port=22, username='ubuntu',password='', pkey=mykey)
    sftp = ssh.open_sftp()
    sftp.put('/home/ubuntu/research_platform/research_platform/research_platform/static/'+file_name, '/home/ubuntu/'+file_name)
    ssh.close()
if __name__ == "__main__":
    main(sys.argv[1])
