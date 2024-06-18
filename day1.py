# day1.py
from aoc_api import *
import sys

def part1(data : list[str]):
    ans = 0
    for i in range(1, len(data)):
            if(int(data[i]) - int(data[i-1]) > 0):
                ans += 1
    return ans

def part2(data : list[str]):
    ans = 0
    sum1 = -1
    sum2 = 0
    for i in range(0, len(data) - 2):
        for window in range(i, i + 3):
            sum2 += int(data[window])
        if(sum1 == -1):
            sum1 = sum2
            sum2 = 0
            continue
        if(sum2 > sum1):
            ans += 1
        sum1 = sum2
        sum2 = 0

    return ans























# auto generated code
solve = sys.argv[1]
inp = get_input(1)
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
    submit(1, solve, ans)

except Exception as e:
    print(e)