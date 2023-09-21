import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "3895dad156f04ea2583e110902afaae6"


def get_temp_zip(zcode):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(zcode)
    response = requests.get(api_url, headers={'X-Api-Key': 'E4F6AJeE8pMzz+5rNO0oFQ==qK05I8OGsTcCZFE5'}).json()
    cTemp = response['temp']
    return celcius_to_fahrenheit(cTemp)
        
def get_wind_zip(zcode):
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(zcode)
    response = requests.get(api_url, headers={'X-Api-Key': 'E4F6AJeE8pMzz+5rNO0oFQ==qK05I8OGsTcCZFE5'}).json()
    return response['wind_speed']

def celcius_to_fahrenheit(cTemp):
    fTemp = cTemp * (9/5) + 32
    return fTemp

def kelvin_to_fahrenheit(kTemp):
    cTemp = kTemp - 273.15
    fTemp = cTemp * (9/5) + 32
    return fTemp


def get_temp_city(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()

    kTemp = response['main']['temp']
    return kelvin_to_fahrenheit(kTemp)
    
def get_wind_city(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()

    wspeed = response['wind']['speed']
    realSpeed = wspeed * (25/11)
    return realSpeed



def main():
    while True:
        answer = input("Would you like to input zip code (US only) or city (name, state, country)? Press z for zip code or c for city  ")
        if answer == 'z':
            zcode = input("What zip code do you want to check the weather for?  ")
            print("Today in " + zcode + " the temperature will be " + str(round(get_temp_zip(zcode))) + " degrees with wind speeds of " +
                  str(round(get_wind_zip(zcode))) + " miles per hour")
            break
        elif answer == 'c':
            city = input("What city do you want to check the weather of?  ")
            print("Today in " + city + " the temperature will be " + str(round(get_temp_city(city))) + " degrees with wind speeds of " + 
                  str(round(get_wind_city(city))) + " miles per hour")
            break
        else:
            print("Please enter z or c")
    

main()