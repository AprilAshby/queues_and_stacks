class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def length(self):
        return len(self.items)


def checker(left, right):
    return left == '(' and right == ')' or left == '[' and right == ']' or left == '{' and right == '}'


def isLeft(x):
    return x == '(' or x == '[' or x == '{'


def validBracketSequence(sequence):
    holding = Stack()
    parens = list(sequence)

    if sequence == "":
        return True

    for each in parens:
        if isLeft(each):
            holding.push(each)
        elif holding.length() < 1 or not checker(holding.pop(), each):
            return False
    return holding.length() == 0
