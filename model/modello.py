from time import time
from functools import lru_cache
import copy

class Model:
    def __init__(self):
        self.lista_soluzioni = []
        self.set_soluzioni = set() # per non avere doppioni (cambiare codice sotto)

    def calcola_anagrammi(self, parola: str):
        self.lista_soluzioni = [] # resetto l'attributo di classe
        self._ricorsione("", parola)
        return self.lista_soluzioni

    @lru_cache(maxsize=None)  # più veloce (se alcune lettere si ripetono)
    def _ricorsione(self, parziale, rimanenti):
        if len(rimanenti) == 0:   # condizione terminale: quando non ci sono più rimanenti
            self.lista_soluzioni.append(parziale)
        else:
            for i in range(len(rimanenti)):
                parziale += rimanenti[i]
                # chiamare ricorsione con parziale e tutte le lettere rimanenti meno rimanenti[i]
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
                self._ricorsione(parziale, nuove_rimanenti)
                # backtracking
                parziale = parziale[:-1] # tutte le lettere tranne l'ultima


    def calcola_anagrammi_list(self, parola: str):
        self.lista_soluzioni = [] # resetto l'attributo di classe
        self._ricorsione_list([], parola)
        # "dog" -> ["d", "o", "g"]
        return self.lista_soluzioni

    def _ricorsione_list(self, parziale, rimanenti):
        if len(rimanenti) == 0:
            self.lista_soluzioni.append(copy.deepcopy(parziale))  # se non faccio la copia ho una lista di liste vuote
        else:
            for i in range(len(rimanenti)):
                parziale.append(rimanenti[i])
                nuove_rimanenti = rimanenti[:i] + rimanenti[i+1:]
                self._ricorsione_list(parziale, nuove_rimanenti)
                # backtracking
                parziale.pop() # tolgo l'ultimo elemento

if __name__ == "__main__":
    model = Model()
    start_time = time()
    risultato = model.calcola_anagrammi("dog")
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(risultato) # con la cache non calcola i doppioni