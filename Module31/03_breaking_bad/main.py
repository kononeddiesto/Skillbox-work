import requests
import json


death_req = requests.get('https://breakingbadapi.com/api/deaths')
data = json.loads(death_req.text)
count_deaths = 0
episode = 0
for i in data:
    if count_deaths < i['number_of_deaths']:
        count_deaths = i['number_of_deaths']
        episode = i['episode']

print('Эпизод: {} количество смертей: {}'.format(episode, count_deaths))

with open('death_file.json', 'w') as file:
    json.dump({episode: count_deaths}, file)
