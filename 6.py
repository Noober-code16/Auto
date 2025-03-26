def epsilon_closure(epsilon_nfa, state, closure):
    """Finds the epsilon closure for a given state."""
    if state not in closure:
        closure.add(state)
        for next_state in epsilon_nfa.get((state, 'E'), []):
            epsilon_closure(epsilon_nfa, next_state, closure)

def get_epsilon_closures(epsilon_nfa, states):
    """Computes epsilon closures for all states."""
    closures = {state: set() for state in states}
    for state in states:
        epsilon_closure(epsilon_nfa, state, closures[state])
    return closures

def convert_to_nfa(epsilon_nfa, states, alphabet):
    """Converts an Epsilon-NFA to an NFA by removing epsilon transitions."""
    epsilon_closures = get_epsilon_closures(epsilon_nfa, states)
    nfa = {}

    for state in states:
        nfa[state] = {}
        for symbol in alphabet:
            reachable = set()
            for s in epsilon_closures[state]:
                reachable.update(epsilon_nfa.get((s, symbol), []))
            nfa[state][symbol] = set().union(*[epsilon_closures.get(s, {s}) for s in reachable])

    return nfa

def get_next_states(nfa, states, symbol):
    """Finds the next states in NFA for a given symbol."""
    next_states = set()
    for state in states:
        next_states.update(nfa.get(state, {}).get(symbol, []))
    return sorted(next_states)

def convert_nfa_to_dfa(nfa, alphabet):
    """Converts an NFA to a DFA using the subset construction method."""
    dfa = {}
    initial_state = tuple(sorted(get_next_states(nfa, ['q0'], 'E')))  # Start with ε-closure of q0
    states_to_process = [initial_state]
    visited = set()

    while states_to_process:
        current = tuple(states_to_process.pop(0))
        if current in visited:
            continue
        visited.add(current)
        
        dfa[current] = {}
        for symbol in alphabet:
            next_state = tuple(get_next_states(nfa, current, symbol))
            dfa[current][symbol] = next_state
            if next_state and next_state not in visited:
                states_to_process.append(next_state)

    return dfa

def main():
    alphabet = ['0', '1']
    epsilon_nfa = {}
    n = int(input("Enter number of states in Epsilon-NFA: "))
    states = [f'q{i}' for i in range(n)]

    for state in states:
        for symbol in ['E', '0', '1']:
            epsilon_nfa[(state, symbol)] = input(f"Enter transitions for ({state}, {symbol}): ").split()

    print("\nEpsilon-NFA Transition Table:")
    for key, value in epsilon_nfa.items():
        print(f"{key} -> {value}")

    # Convert to NFA
    nfa = convert_to_nfa(epsilon_nfa, states, alphabet)
    
    print("\nNFA Transition Table:")
    for state, transitions in nfa.items():
        print(f"{state}: {transitions}")

    # Convert to DFA
    dfa = convert_nfa_to_dfa(nfa, alphabet)
    
    print("\nDFA Transition Table:")
    for state, transitions in dfa.items():
        print(f"{state}: {transitions}")

if __name__ == "__main__":
    main()
