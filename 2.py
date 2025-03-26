def is_accepted(input_string):
    current_states = {'Q0'}  # Start state
    
    for symbol in input_string:
        next_states = set()
        
        for state in current_states:
            if state == 'Q0':
                if symbol == 'a':
                    next_states.add('Q1')
                else:
                    next_states.add('Q0')
            elif state == 'Q1':
                if symbol == 'b':
                    next_states.add('Q2')
                elif symbol == 'a':
                    next_states.add('Q1')
            elif state == 'Q2':
                if symbol == 'a':
                    next_states.add('Q1')
                else:
                    next_states.add('Q0')
        
        current_states = next_states  # Update current states
    
    return 'Q2' in current_states  # Accept if Q2 is in final states

def main():
    input_string = input("Enter a string: ")
    if is_accepted(input_string):
        print("String is accepted.")
    else:
        print("String is not accepted.")

if __name__ == "__main__":
    main()
