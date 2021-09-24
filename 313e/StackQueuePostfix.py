class Stack (object):
    def __init__ (self):
        self.stack= []
    # add an itemto the top of the stack
    # top could be beginning or end of the list depending on how you design it.
    def push (self, item):
        self.stack.append(item)
    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()
    # it is error-prone because you cannot pop the empty stack.
    # check the item on top of the stack
    def peek (self):
        return self.stack[-1]
    # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)
    # return the number of elements in the stack
    def size (self):
        return len(self.stack)

class Queue (object):
    def __init__ (self):
        self.queue = []
    # add an item to the end of the Queue
    def enqueue (self, item):
        self.queue.append(item)
    # remove an item from the beginning of the Queue
    def dequeue(self):
        return self.queue.pop(0)
    # check if the queue is empty
    def is_empty (self):
        return len(self.queue) == 0
    # return the size of the queue
    def size(self):
        return (len(self.queue))



# Operators : + - * / // % **
# operands : integers, floats
# infix : 2 + 3 (operator between operands)
# prefix : + 2 3
# Postfix : 2 3 +
def operate (oper1, oper2, token):
    expr = str(oper1) + token + str(oper2)
    return eval (expr)

# 4 8 7 + 2 * 3 1 - * +
# 3 4 + 5 *
# 3 4 5 + *
# 7 4 + 3 - 2 5 * /

# postfix
def rpn(s):
    theStack = Stack()

    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    for item in tokens:
        if item in operators:
            oper2 = theStack.pop()
            oper1 = theStack.pop()
            theStack.push(operate (oper1, oper2, item))
        else:
            theStack.push(item)
    return theStack.pop()

# prefix
def stack_pre(s):
    theStack = Stack()

    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    tokens.reverse()
    for item in tokens:
        if item in operators:
            oper1 = theStack.pop()
            oper2 = theStack.pop()
            theStack.push(operate (oper1, oper2, item))
        else:
            theStack.push(item)
    return theStack.pop()

def queue_pre(s):
    theQueue = Queue()

    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    

def main():
    in_file = open("rpn.txt", "r")
    for line in in_file:
        line = line.strip()
        value = stack_pre(line)
        print(line, '=', value)
    in_file.close()

main()
