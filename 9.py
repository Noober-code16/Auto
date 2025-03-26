class PDA:
    def __init__(self):
        self.stack = []  # Stack for storing first half of the string
        self.state = 'q0'  # Initial state is q0
        self.middle_reached = False  # Flag to indicate transition to second half

    def process(self, input_string):
        for symbol in input_string:
            if self.state == 'q0':
                if symbol in {'a', 'b'}:
                    self.stack.append(symbol)  # Push first half onto stack
                elif symbol == 'C':
                    self.state = 'q1'  # Transition to second half upon encountering 'C'
                else:
                    return False  # Reject invalid characters
            elif self.state == 'q1':
                if self.stack and self.stack[-1] == symbol:
                    self.stack.pop()  # Pop stack if matching second half
                else:
                    return False  # Reject if mismatch

        return self.state == 'q1' and not self.stack  # Accept if stack is empty

# Testing the PDA
def test_pda():
    pda = PDA()
    test_cases = [
        ("abCab", True),
        ("aC", True),
        ("aaCaa", True),
        ("abCba", True),
        ("abc", False),  # Invalid character
        ("C", False),  # Only 'C' is not in L
        ("aCb", False),  # Mismatch
    ]
    
    for test_string, expected in test_cases:
        pda = PDA()  # Reset PDA for each test
        mid = test_string.find('C')
        if mid == -1:
            result = False  # No 'C' means invalid input
        else:
            pda.process(test_string[:mid])  # Process first half
            result = pda.process(test_string[mid:])  # Process second half
        print(f"Input: {test_string}, Accepted: {result}, Expected: {expected}")

# Run the test cases
test_pda()
