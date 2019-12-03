import os,paramiko

os.system('scp /home/user/installer.py user@remoteip /home/user')

host = 'host'
user = 'user'
key = "/home/user/.ssh/id_rsa.pub"
port = 22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, key_filename=key, port=port)
stdin, stdout, stderr = client.exec_command('sudo yum install -y postgresql96-server ; sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb ; sudo systemctl enable postgresql-9.6 ; sudo systemctl start postgresql-9.6 ; sudo python installer.py')
stdin.write('123456789\n')

print stdout.readlines()




