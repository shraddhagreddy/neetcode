"""Minimum Stack
Solved 
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
Constraints:

-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks."""



class MinStack:
    
    def __init__(self):
       self.stack=[]
       self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val<=self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            val = self.stack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()
        

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1] 
        

    def getMin(self) -> int:
        if not self.minStack:
            raise IndexError("getMin from empty stack")
        return self.minStack[-1]
