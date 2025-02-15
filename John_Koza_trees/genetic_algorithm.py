from BinaryTree import *
import numpy as np
import random


function_list = ["+", "sqrt", "-", "*", "/"]
terminal_list = ["A"]
valores_terminal = {"A": np.array([0.72, 1.00, 1.52, 5.20, 9.53, 19.1])}
diccionario_longitudes = {"A": len(valores_terminal["A"])}
observations = np.array([0.61, 1.00, 1.84, 11.9, 29.4, 83.5])


def gen_list_function_lists(n_pop, max_list_len):
    result_list = []
    for _ in range(n_pop):
        lenght_list = random.randint(1, max_list_len)
        functions = []
        for _ in range(lenght_list):
            func = random.choice(function_list)
            functions.append(func)
        result_list.append(functions)
    return result_list


def gen_population_ini(function_lists):
    list_trees = []
    for lista in range(len(function_lists)):
        arbol, arbol_lista = build_tree(function_lists[lista])
        fitness = fitness_arbol(arbol)
        list_trees.append((arbol, arbol_lista, fitness))
    return list_trees


def selection(list_trees, porcentaje_seleccion):
    lista_ordenada = sorted(list_trees, key=lambda x: x[2])
    number_pop = int(porcentaje_seleccion * len(list_trees))
    return lista_ordenada[0:number_pop]


def crossover(arbol1, arbol_lista_1, arbol2, arbol_lista_2):
    place_1 = random.choice(arbol_lista_1)
    place_2 = random.choice(arbol_lista_2)
    arbol1_changed = change_subtree(arbol1, place_1, place_2)
    arbol2_changed = change_subtree(arbol2, place_2, place_1)
    return arbol1_changed, arbol2_changed


def mutation(arbol, arbol_lista, tasa_mutacion):
    if random.random() < tasa_mutacion:
        pos_random = random.choice(arbol_lista)
        new_pos = Node()
        new_value = random.choice(function_list+terminal_list)
        new_pos.value = new_value
        if new_value == "A":
            new_pos.left = None
            new_pos.right = None
        elif new_value == "sqrt":
            new_pos.right = None
            new_pos.left = pos_random.left
        else:
            new_pos.left = Node(random.choice(terminal_list))
            new_pos.right = Node(random.choice(terminal_list))
        return change_subtree(arbol, pos_random, new_pos)
    return arbol


def reproduction(arbol1, arbol_lista_1, arbol2, arbol_lista_2, tasa_mutacion):
    child1, child2 = crossover(arbol1, arbol_lista_1, arbol2, arbol_lista_2)
    child1_list = get_list(child1)
    child2_list = get_list(child2)
    child1_mutated = mutation(child1, child1_list, tasa_mutacion)
    child2_mutated = mutation(child2, child2_list, tasa_mutacion)
    list_mutated1 = get_list(child1_mutated)
    list_mutated2 = get_list(child2_mutated)
    fitness_1 = fitness_arbol(child1_mutated)
    fitness_2 = fitness_arbol(child2_mutated)
    child1_total = (child1_mutated, list_mutated1, fitness_1)
    child2_total = (child2_mutated, list_mutated2, fitness_2)
    return child1_total, child2_total


def replacement(list_trees, porcentaje_seleccion):
    parents = selection(list_trees, porcentaje_seleccion)
    num_children = len(list_trees)-len(parents)
    children = []
    count = 0
    while count < num_children:
        dad, mom = random.choice(parents)
        child1, child2 = reproduction(dad[0], dad[1], mom[0], mom[1])
        children.append(child1)
        children.append(child2)
        count += 2
    return parents + children