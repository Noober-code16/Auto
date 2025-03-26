from collections import defaultdict

productions = defaultdict(list)
first = defaultdict(set)
follow = defaultdict(set)
non_terminals = []

def find_first(symbol):
    if symbol.islower() or symbol == '$':
        return {symbol}
    if symbol in first and first[symbol]:
        return first[symbol]
    
    for prod in productions[symbol]:
        if prod == '':
            first[symbol].add('$')
        else:
            for char in prod:
                temp = find_first(char)
                first[symbol] |= (temp - {'$'})
                if '$' not in temp:
                    break
            else:
                first[symbol].add('$')
    return first[symbol]

def find_follow(symbol):
    for head, prods in productions.items():
        for prod in prods:
            for i in range(len(prod)):
                if prod[i] == symbol:
                    if i+1 < len(prod):
                        next_sym = prod[i+1]
                        temp = find_first(next_sym)
                        follow[symbol] |= (temp - {'$'})
                        if '$' in temp:
                            follow[symbol] |= follow[head]
                    else:
                        if head != symbol:
                            follow[symbol] |= follow[head]
    return follow[symbol]

# Input
n = int(input("Enter the no of productions: "))
for _ in range(n):
    prod = input("Enter the production: ").split('=')
    lhs, rhs = prod[0], prod[1]
    non_terminals.append(lhs)
    productions[lhs].append(rhs)

start_symbol = non_terminals[0]
follow[start_symbol].add('$')

for nt in non_terminals:
    find_first(nt)
for nt in non_terminals:
    find_follow(nt)

# Output
for nt in non_terminals:
    print(f"First({nt})={first[nt]}")
    print(f"Follow({nt})={follow[nt]}")