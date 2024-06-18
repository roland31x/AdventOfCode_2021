import json
import os
import requests

with open('cookie.json', 'r') as f:
    cookie = json.load(f)['cookie']

def submit(day, part, answer, year=2021):
    url = f'https://adventofcode.com/{year}/day/{day}/answer'
    r = requests.post(url, 
            headers={
            'User-Agent': "roland31x/pyapi v1.0",
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': "session=" + cookie
            }, 
            data={
                'level': part, 
                'answer': answer
            })
    r.raise_for_status()

    response = r.text
    if 'That\'s the right answer!' in response:
        print(f'Answer for day {day}, part {part} is CORRECT!')
    elif 'That\'s not the right answer' in response:
        print(f'Answer for day {day}, part {part} is WRONG!')
        if 'You gave an answer too recently' in response:
            print('You gave an answer too recently.')
        elif 'too high' in response:
            print('Answer is too high.')
        elif 'too low' in response:
            print('Answer is too low.')
        else:
            print('Error submitting answer.')
    else:
        print('Error submitting answer.')
    