class PDA_L1:
    """PDA for L = {0ⁿ1ᵐ2ᵐ3ⁿ | n, m ≥ 1}"""
    
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def process(self, input_string):
        for symbol in input_string:
            if self.state == 'q0':  # Reading 0s
                if symbol == '0':
                    self.stack.append('0')  # Push '0' onto stack
                elif symbol == '1':
                    self.state = 'q1'  # Transition to handling '1's
                else:
                    return False  # Invalid transition

            if self.state == 'q1':  # Reading 1s
                if symbol == '1':
                    continue  # Ignore '1's
                elif symbol == '2':
                    self.stack.append('2')  # Push '2' onto stack
                    self.state = 'q2'
                else:
                    return False  # Reject if not '1' or '2'

            if self.state == 'q2':  # Reading 2s
                if symbol == '2':
                    self.stack.append('2')  # Push another '2' onto stack
                elif symbol == '3':
                    if self.stack and self.stack[-1] == '2':
                        while self.stack and self.stack[-1] == '2':
                            self.stack.pop()  # Pop all '2's first
                        self.state = 'q3'  # Transition to handling '3's
                    else:
                        return False  # No matching '2' for this '3'
                else:
                    return False  # Invalid transition

            if self.state == 'q3':  # Reading 3s
                if symbol == '3':
                    if self.stack and self.stack[-1] == '0':
                        self.stack.pop()  # Pop matching '0'
                    else:
                        return False  # No matching '0' for this '3'
                else:
                    return False  # Invalid transition

        return not self.stack  # Accept only if stack is empty


# Testing the PDA
def test_pda_l1():
    print("\nTesting PDA for L1 = {0ⁿ1ᵐ2ᵐ3ⁿ | n, m ≥ 1}")
    test_cases = [
        ("011223", True),  # n=1, m=1
        ("0011122233", True),  # n=2, m=2
        ("001111222233", True),  # n=2, m=3 (invalid case, should be False)
        ("0123", False),  # Incorrect order
        ("00111233", False),  # Mismatch in counts
        ("00112233", True),  # Valid case with n=2, m=2
        ("0011223", False), 
         ("0223", False) # Missing a '3'
    ]

    for test_string, expected in test_cases:
        pda = PDA_L1()
        result = pda.process(test_string)
        print(f"Input: {test_string}, Accepted: {result}, Expected: {expected}")


# Run the tests
test_pda_l1()
