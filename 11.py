class PDA_L2:
    """PDA for L = {aⁿb²ⁿ | n ≥ 1}"""

    def __init__(self):
        self.stack = []
        self.state = 'q0'
        self.b_count = 0  # Counter for 'b's

    def process(self, input_string):
        for symbol in input_string:
            if self.state == 'q0':  # Reading 'a's
                if symbol == 'a':
                    self.stack.append('a')  # Push 'a' onto stack
                elif symbol == 'b':
                    self.state = 'q1'  # Transition to processing 'b'
                    self.b_count += 1  # Count the first 'b'
                else:
                    return False  # Reject if any other character appears

            elif self.state == 'q1':  # Reading 'b's
                if symbol == 'b':
                    self.b_count += 1  # Count 'b's
                    if self.b_count % 2 == 0:  # Every two 'b's, pop one 'a'
                        if self.stack and self.stack[-1] == 'a':
                            self.stack.pop()  # Pop 'a' for 2 'b's
                        else:
                            return False  # No matching 'a' for 'b's
                else:
                    return False  # Reject if any other character appears

        return not self.stack and self.b_count % 2 == 0  # Accept if stack is empty and b_count is even


# Testing the PDA
def test_pda_l2():
    print("\nTesting PDA for L2 = {aⁿb²ⁿ | n ≥ 1}")
    test_cases = [
        ("abb", True),  # n = 1, b = 2
        ("aabbbb", True),  # n = 2, b = 4
        ("aaabbbbbb", True),  # n = 3, b = 6
        ("aabb", False),  # Incorrect number of 'b's (b = 2, but should be 4)
        ("aabbb", False),  # Incorrect number of 'b's (b = 3, should be 4)
        ("aaaabbbbbb", True),  # n = 4, b = 8 (valid)
        ("a", False),  # No 'b's present
        ("abbba", False),  # Extra 'a' at the end
        ("ab", False),  # Not enough 'b's (b = 1, should be 2)
    ]

    for test_string, expected in test_cases:
        pda = PDA_L2()
        result = pda.process(test_string)
        print(f"Input: {test_string}, Accepted: {result}, Expected: {expected}")


# Run the tests
test_pda_l2()
