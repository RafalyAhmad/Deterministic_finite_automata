class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
    
    def reset(self):
        self.current_state = self.start_state
    
    def process_symbol(self, symbol):
        if symbol in self.alphabet:
            self.current_state = self.transition_function[self.current_state][symbol]
        else:
            raise ValueError(f"Symbol {symbol} not in alphabet")
    
    def process_string(self, input_string):
        self.reset()
        for symbol in input_string:
            self.process_symbol(symbol)
        return self.current_state in self.accept_states
    
    def is_accepting(self):
        return self.current_state in self.accept_states


# Define the DFA
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': 'q1', '1': 'q0'},
    'q1': {'0': 'q1', '1': 'q2'},
    'q2': {'0': 'q1', '1': 'q0'}
}
start_state = 'q0'
accept_states = {'q2'}

# Create a DFA instance
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Test the DFA
test_strings = ['001', '011', '101', '0101', '110']
results = {s: dfa.process_string(s) for s in test_strings}

print("DFA Results:")
for string, result in results.items():
    print(f"String: {string} -> {'Accepted' if result else 'Rejected'}")
