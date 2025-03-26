class PDA:
    def __init__(self):
        self.stack = []  # Stack for storing 'A'
        self.state = 'q0'  # Initial state is q0
    def reset(self):
        self.stack = []
        self.state = 'q0'
    def process(self, input_string):
        for symbol in input_string:
            if self.state == 'q0':  # In state q0
                if symbol == 'a':
                    self.stack.append('A')  # Push 'A' for each 'a'
                elif symbol == 'b':
                    if self.stack:  # Ensure stack is not empty
                        self.stack.pop()  # Pop one 'A' for each 'b'
                        self.state = 'q1'  # Transition to q1
                    else:
                        return False  # Invalid string, more 'b's than 'a's
            elif self.state == 'q1':  # In state q1
                if symbol == 'b':
                    if self.stack:
                        self.stack.pop()  # Continue popping for 'b'
                    else:
                        return False  # Invalid string, more 'b's than 'a's
                else:
                    return False  # Any 'a' after 'b' is invalid
        
        return self.state == 'q1' and not self.stack  # Accept if stack is empty

# Testing the PDA
def test_pda():
    pda = PDA()

    # Test cases
    test_strings = [
        "aabb",      
        "aaabbb",    
        "ab",        
        "aaabbbab",  
        "aab",       
        "abc",
        "abab"
    ]

    for test_string in test_strings:
        pda.reset()  # Reset the PDA before each test
        result = pda.process(test_string)
        print(f"Input: {test_string} - {'Accepted' if result else 'Rejected'}")

# Run the test cases
test_pda()
