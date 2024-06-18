# AdventOfCode_2021
Solutions for the 2021 Advent of Code event

### In order for this to work after cloning you need to execute these commands:
Create the python virtual environment
```
py -m venv .venv
```

Make sure to also activate the created virtual environment!

Then install the requirements in order to be able to fetch inputs directly from website using your cookie
```
pip install -r requirements.txt
```

### Set your browser cookie
Inside the cookie.json, paste your session cookie from the advent of code website. Cookies can be found on the "Application" tab of the developer menu (F12)
You need this step otherwise you cannot auto fetch the inputs! (You need to manually create the inputs folder and paste the day{number}.txt inputs in there).

### Then for each day execute 
```
py day{number}.py <solve_arg>
```

There are 3 solve arguments: 
```
0 - lists the answers for both parts ( doesn't auto submit)
1 - submits for part 1
2 - submits for part 2
```

For an example you can submit part 1 for day 7 using the command:
```
py day07.py 1
```

### Yes, I like having them in order so we use a padding 0 on single digit days....
