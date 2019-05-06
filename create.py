import time
import digitalocean
from tokens import token
manager = digitalocean.Manager(token=token)
keys = manager.get_all_sshkeys()

#https://www.digitalocean.com/community/questions/high-cpu-droplet-availability-via-the-digtialocean-api
droplet = digitalocean.Droplet(token=token,
   name='buildroot',
   region='ams3', # Amster
   image='ubuntu-18-04-x64', # Ubuntu 14.04 x64
   size_slug='512MB',
   #size_slug='c-16',
   ssh_keys=keys, #Automatic conversion
   backups=False)

droplet.create()

# wait for bringup
completed = False
while not completed:
    actions = droplet.get_actions()
    for action in actions:
        action.load()
        # Once it shows complete, droplet is up and running
        print(action.status)
        if action.status == u'completed':
            completed = True

droplet.load()
ip_address = droplet.ip_address
print(ip_address)
print("waiting for ssh")
time.sleep(5)

# copy script and run it
import os
print("copy setup and run")
os.system("scp -o StrictHostKeyChecking=no setup.sh root@%s:~/" % ip_address)
os.system("ssh -o StrictHostKeyChecking=no root@%s ./setup.sh" % ip_address)
