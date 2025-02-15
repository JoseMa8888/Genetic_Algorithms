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
RESULT_FILE_TXT = "./data/result.txt"
RESULT_FILE_PICKLE = "./data/result.pkl"


def creating_initial_population():
    if not os.path.exists(DATA_FILE):
        func_pop_init = gen_list_function_lists(POBLACION_TOTAL, MAX_LENGHT_FUNC_LIST)
        trees_init = gen_population_ini(func_pop_init)
        with open(DATA_FILE, "wb") as f:
            pickle.dump(trees_init, f)
        return trees_init
    else:
        with open(DATA_FILE, "rb") as f:
            data = pickle.load(f)
        return data


def save_tree_to_txt(binary_tree, lista, fitness):
    tree_representation = binary_tree.print_tree(binary_tree.root) if hasattr(binary_tree, "__str__") else str(binary_tree)
    lista_tree = str(list(map(lambda x: x.value, lista)))
    fitness_tree = str(fitness)
    return tree_representation + "\n" + lista_tree + "\n" + fitness_tree + "\n\n"


def creating_result_file_txt(list_final_tree):
    with open(RESULT_FILE_TXT, "w") as f:
        for arbol in list_final_tree:
            representacion = save_tree_to_txt(arbol[0], arbol[1], arbol[2])
            f.write(representacion)
    print("Trees created")


def creating_result_file_pickle(list_final_tree):
    with open(RESULT_FILE_PICKLE, "wb") as f:
        pickle.dump(list_final_tree, f)
    print("Final result of trees are dumped to a pickeled file")
    

def main():
    trees = creating_initial_population()
    list_mean_fitness = [(0,get_mean_fitness(trees))]
    #arbol, lista, fit = trees[0]
    #save_tree_to_txt(arbol, lista, fit)
    for i in range(1,NUMERO_GENERACIONES+1):
        trees = replacement(trees, PORCENTAJE_SELECCION, TASA_MUTACION)
        list_mean_fitness.append((i,get_mean_fitness(trees)))
    creating_result_file_txt(trees)
    creating_result_file_pickle(trees)




if __name__ == "__main__":
    main()