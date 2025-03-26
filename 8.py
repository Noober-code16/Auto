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
                else:
                    return False  # Reject invalid characters
            elif self.state == 'q1':
                if self.stack and self.stack[-1] == symbol:
                    self.stack.pop()  # Pop stack if matching second half
                else:
                    return False  # Reject if mismatch

        return self.state == 'q1' and not self.stack  # Accept if stack is empty

    def transition(self):
        """ Transition to q1 after first half is stored """
        if self.stack:
            self.state = 'q1'
        else:
            return False  # Reject if empty stack before transition

# Testing the PDA
def test_pda():
    pda = PDA()
    test_cases = [
        ("abba", True),
        ("abab", False),
        ("aa", True),
        ("aabb", False),
        ("abc", False),  # Invalid character
        ("aba", False),  # Empty string is not in L
    ]
    
    for test_string, expected in test_cases:
        pda = PDA()  # Reset PDA for each test
        mid = len(test_string) // 2
        pda.process(test_string[:mid])  # Process first half
        pda.transition()  # Transition state
        result = pda.process(test_string[mid:])  # Process second half
        print(f"Input: {test_string}, Accepted: {result}, Expected: {expected}")

# Run the test cases
test_pda()
