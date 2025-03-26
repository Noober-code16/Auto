def is_accepted(input_string):
    current_state = 'Q0'

    for symbol in input_string:
        if current_state == 'Q0':
            if symbol == 'a':
                current_state = 'Q1'
            else:
                current_state = 'Q0'  # Remain in Q0 if input is not 'a'
        elif current_state == 'Q1':
            if symbol == 'b':
                current_state = 'Q2'
            else:
                current_state = 'Q1'  # Stay in Q1 if more 'a's appear
        elif current_state == 'Q2':
            if symbol == 'a':
                current_state = 'Q1'  # Look for a new 'ab' sequence
            else:
                current_state = 'Q0'  # Reset if an invalid character appears

    return current_state == 'Q2'  # Accept if the final state is Q2

def main():
    input_string = input("Enter a string: ")

    if is_accepted(input_string):
        print("String is accepted.")
    else:
        print("String is not accepted.")

if __name__ == "__main__":
    main()
