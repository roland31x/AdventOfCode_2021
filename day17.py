# day17.py
from aoc_api import *
import sys

def part1(data : list[str]):
    ans = 0

    return ans

def part2(data : list[str]):
    ans = 0

    return ans























# auto generated code
solve = sys.argv[1]
inp = get_input(17)
inp = inp.split('\n')
inp.pop()

try:
    if(solve == '1'):
        ans = part1(inp)
    elif(solve == '2'):
        ans = part2(inp)
    elif(solve == '0'):
        ans1 = part1(inp)
        ans2 = part2(inp)
        print(f'Part 1: {ans1}')
        print(f'Part 2: {ans2}')
        quit()
    else:
        raise Exception('Invalid argument. Use 0(no submit), 1 or 2.')

    print('Submitting for part ' + solve)
    print(ans)
    submit(17, solve, ans)

except Exception as e:
    print(e)