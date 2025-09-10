"""Evaluate Reverse Polish Notation
Solved 
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100]."""



from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack=[]
        for ch in tokens:
            if ch not in "+-/*":
                self.stack.append(int(ch))
            elif ch == "+":
                val1=int(self.stack.pop())
                val2=int(self.stack.pop())
                ans=val1+val2
                self.stack.append(ans)
            elif ch == "-":
                val1=int(self.stack.pop())
                val2=int(self.stack.pop())
                ans=val2-val1
                self.stack.append(ans)
            elif ch == "*":
                val1=int(self.stack.pop())
                val2=int(self.stack.pop())
                ans=val1*val2
                self.stack.append(ans)
            elif ch == "/":
                val1=int(self.stack.pop())
                val2=int(self.stack.pop())
                ans=int(val2/val1)
                self.stack.append(ans)
        return self.stack[-1]