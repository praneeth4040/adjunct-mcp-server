import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_weather(location: str) -> str:
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise Exception("API key not found in environment variables.")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch weather data.")

    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    return f"Weather in {location}: {weather}, Temperature: {temp}°C"
