from stack import Stack


def multi_bracket_validation(input):
    lefty = '({['
    righty = ')}]'
    ss = Stack()

    for item in input:
        if item in lefty:
            ss.push(item)
        elif item in righty:
            if ss.top is None:
                return False
            if righty.index(item) != lefty.index(ss.pop().val):
                return False
    return ss.top is None
