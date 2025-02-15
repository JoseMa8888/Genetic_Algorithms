from BinaryTree import *
import random
from matplotlib import pyplot as plt
import pandas as pd
from genetic_algorithm import *

def main():

    listas_funciones = [['*'], ['sqrt'], ['+', '/'], ['+', 'sqrt', '/', '+', '-'], ['/', '/', '+', '*'], ['-', 'sqrt', '*', '+', '+'], ['-', '/', '/'], ['-', 'sqrt', '*'], ['+', '-'], ['+', '+', '-', '/'], ['+', '/']]
    print("Arbol 1")
    lista1 = listas_funciones[5]
    arbol1, arbol_lista1 = build_tree(lista1)
    arbol1.print_tree(arbol1.root)
    print(list(map(lambda x: x.value, arbol_lista1)))
    """print("Arbol 2")
    lista2 = listas_funciones[3]
    arbol2, arbol_lista2 = build_tree(lista2)
    arbol2.print_tree(arbol2.root)
    print(list(map(lambda x: x.value, arbol_lista2)))
    pos_random1 = random.choice(arbol_lista1)
    pos_random2 = random.choice(arbol_lista2)
    print("position random 1", pos_random1.value)
    print("position random 2", pos_random2.value)
    tree_1_changed = change_subtree(arbol1, pos_random1, pos_random2)
    tree_1_changed.print_tree(tree_1_changed.root)"""
    print("Tree mutated")
    mutated, position_mutated = mutation(arbol1, arbol_lista1)
    mutated.print_tree(mutated.root)
    print("Mutacion", position_mutated)
    #print(fitness_arbol(arbol))
    #print(arbol.height())
    print(list(map(lambda x: x.value, get_list(arbol1))))
    """lista = range(10)
    frecuencias = {}
    for _ in range(100000):
        numero = random.choice(lista)
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1
    serie = pd.Series(frecuencias).sort_index()
    plt.bar(serie.index, serie)
    plt.show()"""
if __name__ == "__main__":
    main()