import requests
import json

url = 'http://localhost:5000/'
headers = {'Content-Type':'application/json'}
rule = 'replacetoken/events'
payload = {""}

r = requests.post(url+rule, headers=headers, data=json.dumps(payload))
print(r.text)
