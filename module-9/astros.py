#Scott Anderson Module 9.2 Assignment

import requests


response = requests.get('http://api.open-notify.org/astros.json')
print("Status Code:", response.status_code)


print("Raw JSON:", response.json())


data = response.json()
print("\nThere are currently", data['number'], "astronauts in space:\n")

for person in data['people']:
    print(f"Name: {person['name']} - Craft: {person['craft']}")
