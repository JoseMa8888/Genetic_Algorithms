import math
import random
import numpy as np

function_list = ["+", "sqrt", "-", "*", "/"]
terminal_list = ["A"]
valores_terminal = {"A": np.array([0.72, 1.00, 1.52, 5.20, 9.53, 19.1])}
diccionario_longitudes = {"A": len(valores_terminal["A"])}
observations = np.array([0.61, 1.00, 1.84, 11.9, 29.4, 83.5])

class Node:
    def __init__(self, value=None):
        self.value = value  # El valor del nodo
        self.left = None    # Hijo izquierdo
        self.right = None   # Hijo derecho


class BinaryTree:
    def __init__(self):
        self.root = None  # Raíz del árbol

    # Método para insertar un nodo en el árbol (en este caso, de manera simple)
    def set_root(self, node):
        self.root = node

    def print_tree(self, node, level=0):
        if node:
            print(" " * level * 2 + str(node.value))  # Mostrar el valor del nodo con indentación
            if node.left:
                self.print_tree(node.left, level + 1)  # Recursión para imprimir los hijos
            if node.right:
                self.print_tree(node.right, level + 1)

    def height(self):
        def height_aux(pos, height):
            if not pos:
                return height
            else:
                height_left = height_aux(pos.left, height + 1)
                height_right = height_aux(pos.right, height + 1)
                if height_left > height_right:
                    return height_left
                return height_right
            
        return height_aux(self.root, 0) - 1

def build_tree(function_list):
    arbol = BinaryTree()
    raiz = Node(function_list[0])

    def build_tree_aux(pos, function_list, pos_function, arbol_lista):
        if pos_function >= len(function_list):  # Si no hay más funciones
            if pos.value == "sqrt":  # sqrt solo tiene un hijo
                pos.left = Node(random.choice(terminal_list))
                pos.right = None
                arbol_lista.append(pos.left)
            else:  # Otros operadores tienen dos hijos
                pos.left = Node(random.choice(terminal_list))
                pos.right = Node(random.choice(terminal_list))
                arbol_lista.append(pos.left)
                arbol_lista.append(pos.right)
            return pos, pos_function, arbol_lista

        if pos.value in terminal_list:  # Si el nodo es un terminal, terminamos
            return pos, pos_function, arbol_lista

        else: 
        # Decidir si el lado izquierdo es una función o un terminal
            if random.randint(0, 1) == 0 and pos_function < len(function_list):
                posicion_left = Node(function_list[pos_function])
                arbol_lista.append(posicion_left)
                pos.left, pos_function, arbol_lista = build_tree_aux(posicion_left, function_list, pos_function + 1, arbol_lista)
            else:
                pos.left = Node(random.choice(terminal_list))
                arbol_lista.append(pos.left)
            
            if pos.value != "sqrt":
            # Decidir si el lado derecho es una función o un terminal
                if random.randint(0, 1) == 0 and pos_function < len(function_list):
                    posicion_right = Node(function_list[pos_function])
                    arbol_lista.append(posicion_right)
                    pos.right, pos_function, arbol_lista = build_tree_aux(posicion_right, function_list, pos_function + 1, arbol_lista)
                else:
                    pos.right = Node(random.choice(terminal_list))
                    arbol_lista.append(pos.right)
            return pos, pos_function, arbol_lista

    raiz, _, arbol_list = build_tree_aux(raiz, function_list, 1, [])
    arbol.set_root(raiz)
    return arbol, arbol_list


def fitness_arbol(arbol):
    def fitness_arbol_aux(node):
        if node.value in terminal_list:
            valor = valores_terminal[node.value]
            return valor
        else:
            valor_left = fitness_arbol_aux(node.left) if node.left else (np.zeros(diccionario_longitudes["A"]))
            valor_right = fitness_arbol_aux(node.right) if node.right else (np.zeros(diccionario_longitudes["A"]))
            valor = calculo(node.value, valor_left, valor_right)
            return valor

    resultado = fitness_arbol_aux(arbol.root)
    return np.log(np.linalg.norm(resultado-observations))


def calculo(funcion, valor1, valor2):
    match funcion:
        case "sqrt":
            return np.sqrt(valor1)
        case "*":
            return valor1 * valor2
        case "+":
            return valor1 + valor2
        case "-":
            return valor1 - valor2
        case "/":
            return np.divide(valor1, valor2, where=valor2 != 0)  # Evitar división por cero
        case _:
            raise ValueError(f"Operador desconocido: {funcion}")
    
def get_list(arbol):
    def get_list_aux(pos, lista):
        if pos:
            if pos.left:
                lista.append(pos.left)
                lista = get_list_aux(pos.left, lista)
            if pos.right:
                lista.append(pos.right)
                lista = get_list_aux(pos.right, lista)
            return lista
        return lista
    return get_list_aux(arbol.root, [])


def change_subtree(tree, own_pos, pos_subtree):
    def change_subtree_aux(parent, child, is_left):
        if child is None:
            return False 
        
        if child == own_pos:
            if parent is None:
                tree.root = pos_subtree
            elif is_left:
                parent.left = pos_subtree
            else:
                parent.right = pos_subtree
            return True  
        
        return (change_subtree_aux(child, child.left, True) or
                change_subtree_aux(child, child.right, False))
    
    change_subtree_aux(None, tree.root, False)
    return tree 