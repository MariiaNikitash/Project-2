from collections import deque

def analyze(inp: str) -> None:
    # acepted once top of stack == 1 and input buffer == '$'

    # {acepted_input: next state}
    shifts = {
    '0id': '5',
    '0(': '4',
    '1+': '6',
    '2*': '7',
    '4id': '5',
    '4(': '4',
    '6id': '5',
    '6(': '4',
    '7id': '5',
    '7(': '4',
    '8+': '6',
    '8(': '11',
    '9*': '7'
}   

# { state+input: [variable: char, pop_count: int] }
    reduce = {
    '2+': ['F', 2],
    '2)': ['F', 2],
    '2$': ['F', 2],
    '3+': ['T', 2],
    '3)': ['T', 2],
    '3$': ['T', 2],
    '5+': ['F', 2],
    '5*': ['F', 2],
    '5)': ['F', 2],
    '5$': ['F', 2],
    '9+': ['E', 6],
    '9)': ['E', 6],
    '9$': ['E', 6],
    '10+': ['T', 6],
    '10)': ['T', 6],
    '10$': ['T', 6],
    '11+': ['F', 6],
    '11)': ['F', 6],
    '11*': ['F', 6],
    '11$': ['F', 6]
}

# {state+input: next_state}
    got_to = {
    '0E' : '1',
    '0T' : '2',
    '0F' : '3',
    '4E' : '8',
    '4T' : '2',
    '4F' : '3',
    '6T' : '9',
    '6F' : '3',
    '7F' : '10',
}
    stack, q = ['0'], deque([line for line in inp.split(' ')])


