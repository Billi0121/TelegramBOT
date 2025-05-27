import requests 

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={Moscow}")
print(response.json())