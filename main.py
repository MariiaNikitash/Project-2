from collections import deque
from tabulate import tabulate


class Analyzer:
    def __init__(self, input_tokens: str):
        self.q = deque([line for line in input_tokens.split(' ')])
        self.stack = ['0']

        # not important, using extra space for stdout 
        self.stack_table, self.input_table, self.action_table = [], [], []

    def validShift(self, inp: str) -> str:
        # inp = state + terminal
        # {inp : next state}
        shift = {
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
        '8)': '11',
        '9*': '7'
    }
        return shift[inp] if inp in shift else ''

    def validReduce(self, inp: str) -> str:
        # inp = state + terminal
        # { inp : [reduce_num: char, variable: char, pop_count: int] }
        reduce = {
        '2+': ['2', 'E', 2],
        '2)': ['2', 'E', 2],
        '2$': ['2', 'E', 2],
        '3+': ['4', 'T', 2],
        '3)': ['4', 'T', 2],
        '3$': ['4', 'T', 2],
        '3*': ['4', 'T', 2],
        '5+': ['6', 'F', 2],
        '5*': ['6', 'F', 2],
        '5)': ['6', 'F', 2],
        '5$': ['6', 'F', 2],
        '9+': ['1', 'E', 6],
        '9)': ['1', 'E', 6],
        '9$': ['1', 'E', 6],
        '10+': ['3', 'T', 6],
        '10)': ['3', 'T', 6],
        '10$': ['3', 'T', 6],
        '11+': ['5', 'F', 6],
        '11)': ['5', 'F', 6],
        '11*': ['5', 'F', 6],
        '11$': ['5', 'F', 6]
    }
        return reduce[inp] if inp in reduce else ''

    def validGoTo(self, inp: str):
        # inp = state + variable
        # {inp: next_state}
        go_to = {
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
        return go_to[inp] if inp in go_to else ''

    def find_path() -> None:

        while self.stack and (self.stack[-1] + q[0] in shift or stack[-1] + q[0] in reduce):
            stack_table.append(stack.copy())
            input_table.append(q.copy())

            state, inp = stack[-1], q[0]
            curr_buff = state+inp
            if curr_buff in shift:
                inp = q.popleft()
                nxt_state = shift[curr_buff]
                stack.append(inp)
                stack.append(nxt_state)
                action_table.append(f'Shift {nxt_state}')
            elif curr_buff in reduce:
                reduce_gram, nxt_var, pop_count = reduce[curr_buff]
                for _ in range(pop_count):
                    stack.pop()
                nxt_go_to = stack[-1] + nxt_var
                if nxt_go_to in go_to:
                    nxt_go_to_state = go_to[nxt_go_to]
                    stack.append(nxt_var)
                    stack.append(nxt_go_to_state)
                    action_table.append(f'Reduce {reduce_gram}') 

        stack_table.append(stack.copy())
        input_table.append(q.copy())
        action_table.append('Accepted') if stack[-1] == '1' and q[0] == '$' else action_table.append('Not Accepted')

        print(tabulate({'Stack': stack_table, 'Input': input_table, 'Action': action_table}, headers='keys'))
        print('\n\n')


analyze('( id + id ) * id $')
analyze('id * id $')
analyze('( id * ) $')
