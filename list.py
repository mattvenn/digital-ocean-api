#!/usr/bin/env python
import digitalocean
from tokens import token
manager = digitalocean.Manager(token=token)
my_droplets = manager.get_all_droplets()
for d in my_droplets:
    print(d, d.ip_address)
