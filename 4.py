def get_next_states(nfa, states, symbol):
    """Returns the next states for a given set of states and input symbol."""
    next_states = set()
    for state in states:
        next_states.update(nfa.get((state, symbol), []))
    return sorted(next_states)

def main():
    # Read number of states in NFA
    n = int(input("Enter number of states in NFA: "))
    nfa = {}
    
    # Read NFA transitions
    for i in range(n):
        for symbol in [0, 1]:
            state = f'q{i}'
            nfa[(state, symbol)] = input(f"Enter transitions for ({state}, {symbol}): ").split()
    
    print("\nNFA Transition Table:")
    for (state, symbol), next_states in nfa.items():
        print(f"({state}, {symbol}) -> {next_states}")
    
    # Convert NFA to DFA
    dfa = {}
    states_to_process = [['q0']]  # Start state
    visited = set()
    
    while states_to_process:
        current = tuple(states_to_process.pop(0))
        if current in visited:
            continue
        visited.add(current)
       
        for symbol in [0, 1]:
            next_state = get_next_states(nfa, current, symbol)
            dfa[(current, symbol)] = next_state
            if next_state and tuple(next_state) not in visited:
                states_to_process.append(next_state)
    
    print("\nDFA Transition Table:")
    for (state, symbol), next_state in dfa.items():
        print(f"{state} -- {symbol} --> {next_state}")

if __name__ == "__main__":
    main()
