#!/usr/bin/env python
import digitalocean
from tokens import token
mattvenn = 16303456
manager = digitalocean.Manager(token=token)
my_droplets = manager.get_all_droplets(tag_name="moviepy")
for droplet in my_droplets:
    print(droplet, droplet.ip_address)
    if droplet.id == mattvenn:
        print("somehow got mattvenn droplet!")
        exit(1)
    else:
        answer = raw_input("destroy? [yes]")
        if answer == "yes":
            droplet.destroy()

