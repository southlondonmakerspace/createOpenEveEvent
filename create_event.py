#!/usr/bin/env python3
""" Helper script for WELCOME team
    parse openeve.md for date object and create a new event on discourse
    2025-01-07"""

import os
from datetime import datetime
import re
import requests
from dotenv import load_dotenv

load_dotenv()

def load_content():
    content = "" # because it looks neat.
    filename = "openevening.md" #POSIX PLZ!
    try:
        with open(filename, "r") as file:
            content = file.read()
    except Exception as error:
        print(f"ERROR: File '{filename}' not found")

    return content

def find_datetime(input_string):
    re_pattern = r"\*\*Date\*\* : \w+, (\w+ \d+(?:st|nd|rd|th)?, \d{4})"
    match = re.search(re_pattern, input_string)
    try:
        date_str = match.group(1)
    except AttributeError:
        print("ERROR: Date not found")
        return

    cleaned_date = re.sub(r"(st|nd|rd|th)", "", date_str)
    date_obj = datetime.strptime(cleaned_date, "%B %d, %Y")
    
    return date_obj


def create_new_event():
    headers = {'User-Api-Key': os.getenv('USER_API_KEY'),
               'User-Api-Client-Id': os.getenv('USER_API_CLIENT_ID'),
               'Content-Type': 'application/x-www-form-urlencoded',
               }

    base_url = 'https://discourse.southlondonmakerspace.org'
    
    content = load_content()

    date_obj = find_datetime(content)
    event_date_str = date_obj.strftime("%Y-%m-%d") # 2025-01-22
    event_title_str = date_obj.strftime("%a %w %B") # Wed 22 January
    
    content.replace('"', '\\w') # make sure to escape the "
    data = {
        "title": f"Open Evening {event_title_str}, 7-9pm",
        "raw": content,
        "category": 101,  
        "tags[]": ["openevening"],
        "event[start]": f"{event_date_str}T19:00:00.000Z",
        "event[end]": f"{event_date_str}T21:00:00.000Z",
        "event[timezone]": "Europe/London",
        "event[all_day]": "false",
        "event[deadline]": "false",
        "archetype": "regular",
    }

    url = base_url + '/posts.json'

    print(data)
    response = requests.post(url, headers=headers, data=data)
    return response


def main():
    response = create_new_event()
    return response

if __name__== '__main__':
    main()
