import requests

apirequest = input()
url = "https://pokeapi.co/api/v2/pokemon/{}/".format(apirequest)

response = requests.get(url)

if response.status_code != 200: 
    print("Error")
else:
	data = response.json()
	names = [it["move"]["name"] for it in data["moves"]]
	print(names)