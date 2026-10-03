import requests
 
 
city = input("Enter a city: ").lower()
 
url = f"https://wttr.in/{city}?format=j1"
 
response = requests.get(url)
 
 
if response.status_code == 200:
    data = response.json()
 
    weather = data["current_condition"][0]
 
    print()
    print("===== Weather =====")
    print(f"City: {city.title()}")
    print(f"Temperature: {weather['temp_C']}°C")
    print(f"Feels like: {weather['FeelsLikeC']}°C")
    print(f"Weather: {weather['weatherDesc'][0]['value']}")
 
else:
    print("City not found!")
