import digitalocean
from tokens import token
manager = digitalocean.Manager(token=token)
my_droplets = manager.get_all_droplets()
print(my_droplets)