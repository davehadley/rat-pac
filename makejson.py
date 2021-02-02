import os
env = os.environ

for k,v in sorted(env.items()):
	print(f"\"{k}\" : \"{v}\",")
