"""
@author: Ms. Namasivayam, Liliana Dhaliwal
"""

class FSM:
    def __init__(self, initial_state):
        # Dictionary (input_symbol, current_state) --> (action, next_state).
        self.state_transitions = {}
        self.current_state = initial_state

    # Adds a transition to the dictionary of transitions
    def add_transition(self, input_symbol, state, action=None, next_state=None):
        if next_state is None:
            self.state_transitions[(input_symbol, state)] = (action, self.current_state)
        else:
            self.state_transitions[(input_symbol, state)] = (action, next_state)

    # Returns a transition according to an input and current state
    def get_transition(self, input_symbol, state):
        return self.state_transitions[(input_symbol, state)]
    
    # Carries out a transition
    def process(self, input_symbol):
        (action, next_state) = self.get_transition(input_symbol, self.current_state)
        
        if action is not None:
            action()

        self.current_state = next_state