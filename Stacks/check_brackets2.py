
def check_brackets(text):
    stack = []
    dic = {'{' : '}', '[' : ']', '(' : ')'}
    for i, c in enumerate(text):
        if c in dic:
            stack.append((i,c))
        if c in ['}', ']', ')']:
            if len(stack) == 0:
                return i + 1
            else:
                if c == dic[stack[-1][1]]:
                    stack.pop()
                else:
                    return i + 1
    if len(stack) == 0:
        return "Success"
    else:
            return stack[-1][0] + 1
    
def main():
    text = input()
    print(check_brackets(text))

if __name__ == "__main__":
    main()
 
        
        
