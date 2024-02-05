#-------------------------------------------------------------------------------
# Authors:     Diana Fernadez       #21747
#              Jennifer Toxcon      #21276      
#
# Finished:     22/11/2023
#-------------------------------------------------------------------------------
import yaml

class TapeNode:
    def __init__(self, value, prev=None, nextNode=None):
        self.value = value
        self.prev = prev
        self.nextNode = nextNode

class TuringMachine:
    def __init__(self, config_file):
        with open(config_file, 'r', encoding='utf-8') as file:
            self.config = yaml.safe_load(file)

        # Configuración inicial de la máquina de Turing
        self.states = self.config.get('q_states', {}).get('q_list', [])
        self.initial_state = self.config.get('q_states', {}).get('initial', '')
        self.final_state = self.config.get('q_states', {}).get('final', '')
        self.alphabet = self.config.get('alphabet', [])
        self.tape_alphabet = self.config.get('tape_alphabet', [])
        self.transitions = self.config.get('delta', [])
        self.simulation_strings = self.config.get('simulation_strings', [])
        self.head = TapeNode(value=None)

        # Estado actual y cinta
        self.current_state = self.initial_state

    def display_configuration(self):
        print("Configuración de la Máquina de Turing:")
        print(f"Estados: {self.states}")
        print(f"Estado Inicial: {self.initial_state}")
        print(f"Estado Final: {self.final_state}")
        print(f"Alfabeto: {self.alphabet}")
        print(f"Alfabeto de la Cinta: {self.tape_alphabet}")
        print(f"Delta: {self.transitions}")
        print(f"Cadenas de Simulación: {self.simulation_strings}")

        self.load_transitions()

    def load_transitions(self):
        self.transition_dict = {}
        for transition in self.transitions:
            key = (transition['params']['initial_state'], transition['params']['tape_input'])
            value = (transition['output']['final_state'], transition['output']['tape_output'], transition['output']['tape_displacement'])

            # Almacenar múltiples transiciones para un mismo estado y símbolo
            if key not in self.transition_dict:
                self.transition_dict[key] = []
            self.transition_dict[key].append(value)

            print(f"Transición: {key} -> {value}")
    
    def move_head(self, direction):
        if direction == 'L':
            if self.head.prev is None:  
                new_node = TapeNode(value=' ')
                new_node.nextNode = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                self.head = self.head.prev
        elif direction == 'R':
            if self.head.nextNode is None:
                new_node = TapeNode(value=' ')
                new_node.prev = self.head
                self.head.nextNode = new_node
                self.head = new_node
            else:
                self.head = self.head.nextNode

    def get_possible_transitions(self, state, symbol):
        return self.transition_dict.get((state, symbol), [])

    def update_tape(self, write_symbol, move_direction):
        # Actualizar el valor en la cinta
        self.head.value = write_symbol if write_symbol is not None else self.head.value
        # Mover la cabeza lectora/escritora
        self.move_head(move_direction)
    
    def load_tape(self, input_string):
        self.head = TapeNode(value=input_string[0])
        current_node = self.head
        for char in input_string[1:]:
            new_node = TapeNode(value=char)
            current_node.nextNode = new_node
            new_node.prev = current_node
            current_node = new_node

    def simulate_step(self):
        current_symbol = self.head.value if self.head.value is not None else ' '  # Manejo de espacios en blanco
        possible_transitions = self.get_possible_transitions(self.current_state, current_symbol)

        if not possible_transitions:
            print(f"Transición no definida para el símbolo {current_symbol} y estado {self.current_state}")
            return False

        # Elige una transición de las posibles
        next_state, write_symbol, move_direction = possible_transitions[0]
        self.update_tape(write_symbol, move_direction)
        self.current_state = next_state
        return True
    
    def simulate(self):
        for input_string in self.simulation_strings:
            self.load_tape(input_string)

        step_count = 1

        while self.current_state != self.final_state:
            print(f"Paso {step_count}: {self.display_tape(with_state=True)}")  # Mostrar el estado antes de cada paso
            if not self.simulate_step():
                break
            step_count += 1

        print(f"\nPaso Final {step_count}: {self.display_tape(with_state=True)}")  # Mostrar el estado final
        print(f"Original: {self.display_tape(original=True)}")
        print(f"Resultado: {self.display_tape()}")

    def display_tape(self, original=False, with_state=False):
        tape_str = ""
        # Comenzar desde el nodo más a la izquierda
        node = self.head
        while node.prev:
            node = node.prev

        # Recorrer toda la cinta hasta el final
        while node:
            if node == self.head and with_state:
                tape_str += f"[{self.current_state}] "
            tape_value = node.value if node.value is not None else ' '
            tape_str += f"[{tape_value}] "
            node = node.nextNode

        return tape_str.strip()

def main():
    tm = TuringMachine('Mt3.yaml')
    tm.display_configuration()

    for input_string in tm.simulation_strings:
        print(f"\nSimulación para la cadena: {input_string}")

        # Simular hasta que no haya más pasos posibles o se alcance el estado final
        while tm.current_state != tm.final_state:
            if not tm.simulate():
                break

        if tm.current_state == tm.final_state:
            print("Cadena aceptada.")
        else:
            print("Cadena rechazada.")

if __name__ == "__main__":
    main()
