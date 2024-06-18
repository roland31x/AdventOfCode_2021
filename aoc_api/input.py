import json
import os
import requests

with open('cookie.json', 'r') as f:
    cookie = json.load(f)['cookie']

def get_input(day, year=2021):
    try:
        with open(f'inputs/day{day}.txt', 'r') as f:
            print(f'Input for day {day} found in input/{year}/day{day}.txt')
            return f.read()
    except Exception:       
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        r = requests.get(url, headers= {
            'User-Agent': "roland31x/pyapi v1.0",
            'Content-Type': 'text/plain',
            'Cookie': "session=" + cookie
            })
        r.raise_for_status()
        data = r.text
        with open(f'inputs/day{day}.txt', 'w') as f:
            f.write(data)
        print(f'Input for day {day} fetched and saved to input/{year}/day{day}.txt')
        return data