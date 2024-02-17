#-------------------------------------------------------------------------------
# Authors:     Diana Fernadez       #21747
#              Diego Alonzo         #20172      
#
# Finished:     22/11/2023
#-------------------------------------------------------------------------------
import copy
import yaml
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class Tape(object):   
    blank_symbol = " " 
    def __init__(self,
                 tape_string = "",blank=" "):
        self.__tape = dict((enumerate(tape_string)))
        Tape.blank_symbol = blank
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index+1):
            s += self.__tape[i]
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class MultiTapeTuringMachine(object):
    def __init__(
        self, 
        tapes = list[str],
        blank_symbol = " ",
        initial_state = "",
        final_states = None,
        transition_function = None , accept_states = None):
        self.__blank_symbol = blank_symbol
        self.__init = initial_state
        self.tapes = tapes
        self.__curr = 0
        self.__tapes = [Tape(tape, self.__blank_symbol) for tape in tapes]
        self.__head_positions = [0 for x in range(len(tapes))]
        self.__current_state = initial_state
        self.__immediate_description = None
        self.__accept_states = accept_states
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def evaluate_strings(self):
        print("=================================")
        
        print("Result of the Turing machine calculation:")
        string = "Input on Tape:\n"
        for tape in self.__tapes:
            tape_c = str(tape).replace(self.__blank_symbol, '')
            string+= tape_c+" "
        print(string)
        print("---------------------------------")
        i = 0
        while not self.final():
            self.step()
            i+=1
        print("---------------------------------")
        if (self.__accept_states):
            if self.__current_state in self.__accept_states:
                print("String accepted")
            else:
                print("String not accepted")
        else:
            print("Machine has not accept nor reject")
        print("---------------------------------")
        # print("Result of the Turing machine calculation:")
        # for tape in self.__tapes:
        #     tape_c = str(tape).replace(self.__blank_symbol, '')
        # print(tape_c)
        # print("---------------------------------")
        return
    
    
    def step(self):
        self.generate_immediate_description(True)
        chars_under_heads = [self.__tapes[x][self.__head_positions[x]] for x in range(len(self.__head_positions))]
        x = chars_under_heads
        x.insert(0,self.__current_state)
        x = tuple(x)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            for i in range(len(self.__tapes)):
                self.__tapes[i][self.__head_positions[i]] = y[1][i]
                if y[2][i] == "R":
                    self.__head_positions[i] += 1
                elif y[2][i] == "L":
                    self.__head_positions[i] -= 1
                elif y[2][i] == "S":
                    self.__head_positions[i] -= 0
            self.__current_state = y[0]
        self.generate_immediate_description(False)
            
    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
        
    def generate_immediate_description(self, first:bool):
        # Es un set de descripciones inmediatas
        if (first):
            self.__immediate_description = []
            for k in range(len(self.__tapes)):
                tape = self.__tapes[k]
                self.__immediate_description.append(copy.deepcopy(tape))
                self.__immediate_description[k][self.__head_positions[k]]= bcolors.FAIL +  self.__current_state + bcolors.ENDC +self.__immediate_description[k][self.__head_positions[k]]
        else:
            string = ""
            for k in range(len(self.__tapes)):
                tape = self.__tapes[k]
                immediate_description = copy.deepcopy(tape)
                if k == 0:
                    immediate_description[self.__head_positions[k]]= bcolors.FAIL +  self.__current_state + bcolors.ENDC+self.__immediate_description[k][self.__head_positions[k]]
                else:
                    immediate_description[self.__head_positions[k]]= bcolors.FAIL + bcolors.ENDC+self.__immediate_description[k][self.__head_positions[k]]
                string+=str(self.__immediate_description[k])+" ├─ "+str(immediate_description)+"  "
            print(string)
            

def createTouringMultiTapeFromFile(filename) -> MultiTapeTuringMachine: 
    '''
    Lee un archivo yaml, retorna una maquina de touring com la 
    imformación leída en el yaml
    '''

    with open(filename, 'r') as yaml_file:
        data = yaml.load(yaml_file,Loader=yaml.FullLoader)
        inicial = data['q_states']['initial']
        final = {val for val in data['q_states']['final']}
        acc = {val for val in data['q_states']['accept']}
        blank_symbol = data['blank']
        transition_function = {}
        simulation_strings = data['simulation_strings']
        for params in data['delta']:
            lista_name = params['params']['tape_input']
            lista_name.insert(0, params['params']['initial_state'])
            transition_function[tuple(lista_name)] = (params['output']['final_state'], params['output']['tape_output'], params['output']['tape_displacement'])
        # print(transition_function)
        
        return MultiTapeTuringMachine(tapes= simulation_strings, blank_symbol= blank_symbol, initial_state = inicial, final_states=final,transition_function= transition_function, accept_states= acc)
  
t = createTouringMultiTapeFromFile("./turing.yaml")
# create_turing_machine_graph("./turing4.yaml")
# t = createTouringFromFile("./turing4.yaml")

t.evaluate_strings()