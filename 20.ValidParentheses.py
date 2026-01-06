
def is1Valid(s1):
    
    open_brackets = {'(','[','{'}
    close_brackets = {')',']','}'}
    map_brackets = {
        '(':')',
        '[':']',
        '{':'}'
        }
    
    stack = []
    
    for char in s1:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return False
            top = stack.pop()
            if map_brackets[top] != char:
                return False
    return len(stack) == 0