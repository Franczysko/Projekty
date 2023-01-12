import requests
import random

from pathlib import Path

response = requests.get(f'https://api.dicebear.com/5.x/pixel-art/svg?glassesProbability={random.randrange(0,100)}')

Path('./avatars').mkdir(exist_ok=True)

with open('./avatars/avatar.svg', 'wb') as file:
    file.write(response.content)




