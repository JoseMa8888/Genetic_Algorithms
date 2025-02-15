from genetic_algorithm import *
import os
import pickle
from BinaryTree import *


POBLACION_TOTAL = 128
NUMERO_GENERACIONES = 1000
MAX_LENGHT_FUNC_LIST = 5
PORCENTAJE_SELECCION = 0.1
PROBABILIDAD_ELECCION = 13
TASA_MUTACION = 0.01
DATA_FILE = "./data/datos.pkl"


def creating_initial_population():
    if not os.path.exists("initial_population.txt"):
        func_pop_init = gen_list_function_lists(POBLACION_TOTAL, MAX_LENGHT_FUNC_LIST)
        trees_init = gen_population_ini(func_pop_init)
        with open(DATA_FILE, "wb") as f:
            pickle.dump(trees_init, f)
        return trees_init
    else:
        with open(DATA_FILE, "wb") as f:
            data = pickle.load(f)
        return data
    

def main():
    trees = creating_initial_population()
    arbol, lista, fit = trees[0]
    print(arbol.print_tree(arbol.root))
    print(list(map(lambda x: x.value, lista)))
    print(fit)



if __name__ == "__main__":
    main()