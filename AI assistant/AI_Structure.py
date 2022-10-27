import datetime, random, sys, os, web, subprocess, port_scanner_threaded, pyjokes, speedtest, geocoder
from geopy.geocoders import Nominatim
import python_weather
import asyncio
import os
hello_response = [
    "Hey!",
    "Hello. What can I do for you?",
    "Hello!",
    "Hello. I am your personal assistant.",
    "Hello! How are you?",
    "Hi!",
    "How are you?"
    ]

def str_in_str (str1, str2=[]):
    for i in str2:
        if str1.lower() in i.lower():
            return True
    return False

async def getweather():
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        loc_postition = geocoder.ip('me')
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = str(geolocator.reverse(loc_postition.latlng))
        print('================' + location.split(',')[4] + ' ================')
        weather = await client.get(location.split(',')[4]) 

        print("TEMPERATURE:  " + str(weather.current.temperature), end="\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")

        for forecast in weather.forecasts:
            print(forecast.date, forecast.astronomy, end='\n========================================')
#
            for hourly in forecast.hourly:
                print('\n' + 
                str(hourly.time//100) + ":00  >>>  " + 
                str(hourly.temperature) + '°C || ' + 
                str(hourly.description) + ' ' + 
                str(str(hourly.__repr__).split(' ')[-1].replace("type=", "").replace(">", "").replace(" ", "")), 
                end="\n========================================")
            print("\r<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
        
def main(usr_input):
    if str_in_str("time", usr_input[-1]):
        if str_in_str("what", usr_input[-1]) or str_in_str("what's", usr_input[-1]) or str_in_str("get", usr_input[-1]):
            return (str(datetime.datetime.now().hour)
            + ':'
            + str(datetime.datetime.now().minute)
            + ':'
            + str(datetime.datetime.now().second))
    
    elif str_in_str("date", usr_input[-1]):
        if str_in_str("what", usr_input[-1]) or str_in_str("what's", usr_input[-1]) or str_in_str("get", usr_input[-1]):
            return (str(datetime.datetime.now().year)
            + '-'
            + str(datetime.datetime.now().month)
            + '-'
            + str(datetime.datetime.now().day))

    elif str_in_str("Hello", usr_input[-1]) or str_in_str("hi", usr_input[-1]):
        return random.choice(hello_response)

    elif str_in_str("clear", usr_input[-1]) or str_in_str("cls", usr_input[-1]):
        os.system("cls")
        return "cleared!"
    
    elif str_in_str("search", usr_input[-1]):       
        if str_in_str("web", usr_input[-1]) or str_in_str("internet", usr_input[-1]) or str_in_str("google", usr_input[-1]):
            return "what do you want to search?"
    
    elif str_in_str("map", usr_input[-1]) or str_in_str("direction", usr_input[-1]) or str_in_str("travel", usr_input[-1]):
        return "where do you want to go?"
    
    elif str_in_str("port", usr_input[-1]) or str_in_str("nmap", usr_input[-1]):
        if str_in_str("scan", usr_input[-1]):
            port_scanner_threaded.main()
            return "PORT SCAN COMPLETE"
    
    elif str_in_str("ping", usr_input[-1]):
        print("pong!")
        os.system("speedtest-cli --simple")
        return ""

    elif str_in_str("weather", usr_input[-1]):

        if __name__ != "__main__":
            if os.name == "nt":
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

            asyncio.run(getweather())
        return ""

    elif str_in_str("email", usr_input[-1]) or str_in_str("send", usr_input[-1]) or str_in_str("text", usr_input[-1]):
        web.gmail()
        return ""

    elif str_in_str("joke", usr_input[-1]):
        return pyjokes.get_joke(language='en', category='all')
    
    elif str_in_str("link", usr_input[-1]):
        return "enter link to go to : "

    elif str_in_str("exit", usr_input[-1]) or str_in_str("quit", usr_input[-1]):
        return "EXITING......"
    
    try:
        if str_in_str("search", usr_input[-2]):
            if str_in_str("web", usr_input[-2]) or str_in_str("internet", usr_input[-2]) or str_in_str("google", usr_input[-2]):
                temp_str = ""
                for i in usr_input[-1]:
                    temp_str += i
                web.search(temp_str)
                return ""
        
        elif str_in_str("map", usr_input[-2]) or str_in_str("direction", usr_input[-2]) or str_in_str("travel", usr_input[-2]):
            temp_str = ""
            for i in usr_input[-1]:
                temp_str += i
            web.map(temp_str)
            return ""
        
        elif str_in_str("link", usr_input[-2]):
            temp_str = ""
            for i in usr_input[-1]:
                temp_str += i
            web.open(temp_str)
            return ""
    except:
        pass
    
    return "I don't understand"

