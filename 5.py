def epsilon_closure(epsilon_nfa, state, closure):
    """Finds the epsilon closure for a given state."""
    if state not in closure:
        closure.add(state)
        for next_state in epsilon_nfa.get((state, 'E'), []):
            epsilon_closure(epsilon_nfa, next_state, closure)

def convert_to_nfa(epsilon_nfa, states, alphabet):
    """Converts Epsilon-NFA to NFA by removing epsilon transitions."""
    epsilon_closures = {state: set() for state in states}
    for state in states:
        epsilon_closure(epsilon_nfa, state, epsilon_closures[state])

    nfa = {}
    for state in states:
        nfa[state] = {}
        for symbol in alphabet:
            reachable = set()
            for s in epsilon_closures[state]:
                reachable.update(epsilon_nfa.get((s, symbol), []))
            nfa[state][symbol] = set().union(*[epsilon_closures.get(s, {s}) for s in reachable])

    return nfa

# User input for Epsilon-NFA
alphabet = ['0', '1']
epsilon_nfa = {}
n = int(input("Enter number of states in Epsilon-NFA: "))
states = [f'q{i}' for i in range(n)]

for state in states:
    for symbol in ['E', '0', '1']:
        epsilon_nfa[(state, symbol)] = input(f"Enter transitions for ({state}, {symbol}): ").split()

# Display Epsilon-NFA
print("\nEpsilon-NFA Transition Table:")
for key, value in epsilon_nfa.items():
    print(f"{key} -> {value}")

# Convert to NFA and display results
nfa = convert_to_nfa(epsilon_nfa, states, alphabet)
print("\nNFA Transition Table:")
for state, transitions in nfa.items():
    print(f"{state}: {transitions}")