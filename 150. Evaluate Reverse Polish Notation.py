from typing import List

class Solution:

    def __init__(self) -> None:
        self.operators = ['*', '/', '+', '/']
        pass
    
    def add(self, i, j):
        return i + j
    
    def sub(self, i, j):
        return j - i
    
    def mul(self, i, j):
        return i * j
    
    def div(self, i, j):
        return int(j / i)

    def evalRPN(self, tokens: List[str]) -> int:
        variables = []
        for i in tokens:
            if i not in self.operators:
                variables.append(int(i))
            elif i == '+':
                variables.append(self.add(variables.pop(), variables.pop()))
            elif i == '-':
                variables.append(self.sub(variables.pop(), variables.pop()))
            elif i == '*':
                variables.append(self.mul(variables.pop(), variables.pop()))
            elif i == '/':
                variables.append(self.div(variables.pop(), variables.pop()))
        return variables.pop()



s = Solution()
print(s.evalRPN(["2","1","+","3","*"]))
print(s.evalRPN(["4","13","5","/","+"]))
