# Würfelautomat
# Die Erdbeschleunigung von 1g entsprich einem Messwert von rund 20. 
# Has something to do with a Beschleunigungssensor.
thres = 12 # Measurements under 12 are ignored
def side_up():
    while True:
        x = acc.x(); y = acc.y(); z = acc.z() # Bescheunigungssensoren - essentially it tells it which side is up.
        if x > thres: return 5 #x up
        if x < -thres: return 2 #x down
        if y > thres: return 6 #y up
        if y < -thres: return 1 #y down
        if z > thres: return 3 #z up
        if z < -thres: return 4 #z down
        # no stable situation yet

# Symbolerzeugung
def new_input():
    while True:
        curr = side_up()
        new = curr 
        # gets the current side up as long as it has been up fo rlonger than 500 millisecond
        start = pyb.millis()
        while (curr == new and
                pyb.elapsed_millis(start) <= 500):
            new = side_up()
        if curr == new:
            return curr
# Erzeugt ca. alle 0,5 Sekunden ein neues Eingabesymbol.
# Nicht nur, wenn die Seite gewechselt wird. Daher muss der
# Automat etwas anders aussehen
# Wenn er stillliegt, dann ist curr == new and ein neues Symbol wird generiert

# Übergangsfunktion
def next_state(state, input):
    if state == 0: # intial state
        if input == 5: return 1
        return 0
    elif state == 1: # '5' read
        if input == 5: return 1
        if input == 1: return 2
        if input == 4: return 4
        return 0
    elif state == 2: # '51' read
        if input == 1: return 2 # repetition!
        if input == 5: return 3
        return 0
    elif ...
    # Beachte: Jeder Zustand hat eine Schleife für das Zeichen, das 
    # dafür notwendig war, in den Zustand zu kommen.

    # Der Automat und die Ausgabefunktion

def automaton():
    state = 0
    while True:
        if sw(): return # if switch is pressed, exit.
        state = next_state(state, new_input())
        code_knock(output_symbol(state))

def output_symbol(state):
    if state == 10:
        return "north"
    elif state == 11:
        return "east"
    else:
        return None

