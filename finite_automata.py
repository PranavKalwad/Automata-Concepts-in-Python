#Creating a class DFA.
class DFA:
    current_state=None;
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;

    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;

    def in_accept_state(self):
        return self.current_state in self.accept_states;

    
    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();
    pass;
    

states={0,1,2,3}
alphabet={'a','b'}
tf=dict();

tf[(0,'a')]=1;
tf[(0,'b')]=0;
tf[(1,'a')]=1;
tf[(1,'b')]=2;
tf[(2,'a')]=1;
tf[(2,'b')]=3;
tf[(3,'a')]=1;
tf[(3,'b')]=0;

start_state=0;
accept_states={3}

d = DFA(states, alphabet, tf, start_state, accept_states);

inp_str=input("Enter the string:")

inp_dfa=list(inp_str)

if(d.run_with_input_list(inp_dfa)):
    print("String is accepted")
else:
    print("String is rejected");


