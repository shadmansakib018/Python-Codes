from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reverse_string(s1):
        stack = Stack()
        for char in s1:
            stack.push(char)
        str1 = ""
        while(stack.size()>0):
            str1 = str1 + stack.pop()
        return str1

def get_match(closing,opening):
    bracket_dict = {
    "(" : ")",
    "{": "}",
    "[": "]"
    }
    if(closing == bracket_dict[opening]):
        return True
    return False

def is_balanced(s1):
    stack = Stack()

    for char in s1:
        if(char in ["(", "{", "["]):
            stack.push(char)

        if(char in [")", "}", "]"]):
            if stack.size()>0:
                opening = stack.pop()
                if(not get_match(char, opening)):
                    print("not a match")
                    return False
                else:
                    continue
            else:
                print("starting/ending with a closing brace")
                return False

    if(stack.size()>0):
        print("has opening brace at end")
        return False

    return True







#print(reverse_string("We will conquere COVID-19"))

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g)))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

