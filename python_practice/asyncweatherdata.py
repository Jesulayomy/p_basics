#!/usr/bin/python3
import asyncio
import requests


async def fetch_weather_data(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=035d3c12a9b34d3799224544230508&q={city}"
    response = await asyncio.to_thread(requests.get, url)
    data = response.json()
    return data

async def main():
    cities = ["New York", "Los Angeles", "Chicago"]

    tasks = [fetch_weather_data(city) for city in cities]
    weather_data = await asyncio.gather(*tasks)

    for city, data in zip(cities, weather_data):
        temperature = data['current']['temp_c']
        print(f"Current temperature in {city}: {temperature}°C")

if __name__ == "__main__":
    asyncio.run(main())
