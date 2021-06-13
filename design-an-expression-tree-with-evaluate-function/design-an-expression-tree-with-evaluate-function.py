import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    def __init__(self, _left, _right):
        self.left = _left
        self.right = _right
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""
class Plus(Node):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()
class Minus(Node):
    def evaluate(self):
        return self.right.evaluate() - self.left.evaluate()
class Multiply(Node):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()
class Divide(Node):
    def evaluate(self):
        return self.right.evaluate() // self.left.evaluate()
class Num:
    def __init__(self, value):
        self.value = value
    def evaluate(self):
        return self.value

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        return self.evaluate(postfix)
    def evaluate(self,postfix):
        operators = {'+': Plus, '-': Minus, '*': Multiply, '/': Divide}
        stack = []
        for i in postfix:
            if i in {'+','-','*','/'}:
                a = stack.pop()
                b = stack.pop()
                stack.append(operators[i](a,b))
            else:
                stack.append(Num(int(i)))
        return (stack[0])
        
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        