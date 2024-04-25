import json
import requests
import sys


api_url = 'https://api.api-ninjas.com/v1/cars?limit=5&make=lamborghini&year=2024&model=urus'
response = requests.get(api_url, headers={'X-Api-Key': '+LNP8mg1hDCqYaUM+C6ElQ==xZ3S7GJWP3oQZBvU'})
print(json.dumps(response.json(), indent=2))
