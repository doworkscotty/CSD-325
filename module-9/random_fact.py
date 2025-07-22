#Scott Anderson 9.2 Assignment 

import requests


url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
response = requests.get(url)
print("Status Code:", response.status_code)


print("\nRaw JSON:", response.json())


data = response.json()
print("\nHere's a random fact:")
print(data['text'])
