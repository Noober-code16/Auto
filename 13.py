def generate_3ac(expression):
    temp_count = 1
    stack = []
    postfix = []
    op_stack = []

    precedence = {'+':1, '-':1, '*':2, '/':2}

    # Convert to postfix
    for ch in expression:
        if ch.isalnum():
            postfix.append(ch)
        elif ch in precedence:
            while (op_stack and precedence.get(op_stack[-1], 0) >= precedence[ch]):
                postfix.append(op_stack.pop())
            op_stack.append(ch)

    while op_stack:
        postfix.append(op_stack.pop())

    # Generate 3AC from postfix
    temp_vars = []
    for ch in postfix:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f't{temp_count}'
            temp_vars.append(f"{temp} = {op1} {ch} {op2}")
            stack.append(temp)
            temp_count += 1

    temp_vars.append(f"x = {stack.pop()}")

    print("\nThree Address Code:")
    for code in temp_vars:
        print(code)

# Input example: a+b+c+d (entered as a+b+c+d)
expression = input("Enter the expression: ").replace(" ", "")
generate_3ac(expression)
