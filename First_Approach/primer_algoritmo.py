import random
import functools


POBLACION_TOTAL = 128
PESO_MOCHILA = 9
NUMERO_GENERACIONES = 1000
PORCENTAJE_SELECCION = 0.2
TASA_MUTACION = 0.01
OBJETOS = [
    {"Peso": 2, "Valor": 3},
    {"Peso": 3, "Valor": 4},
    {"Peso": 4, "Valor": 5},
    {"Peso": 5, "Valor": 8}
]


def gen_population(n_population):
    lista_cromosomas = []
    for i in range(n_population):
        lista_cromosomas.append([random.randint(0,1) for i in range(4)])
    return lista_cromosomas


def fitness(cromosoma):
    peso = 0
    valor = 0
    for i in range(len(cromosoma)):
        if cromosoma[i] == 1:
            peso += OBJETOS[i]["Peso"]
            valor += OBJETOS[i]["Valor"]
    if peso > PESO_MOCHILA:
        return 3 -(peso/(peso+1))
    else:
        return valor


def aplicar_fitness(poblacion):
    poblacion_fitness = []
    for cromosoma in poblacion:
        valor = fitness(cromosoma)
        poblacion_fitness.append((cromosoma, valor))
    return poblacion_fitness


def selection(conjunto_cromosomas, porcentaje_seleccion):
    numero_cromosomas = int(POBLACION_TOTAL * porcentaje_seleccion)
    orden_conjunto_cromosomas = sorted(conjunto_cromosomas, key=lambda x: -x[1])
    padres = orden_conjunto_cromosomas[0:numero_cromosomas]
    return padres

 
def mutacion(cromosoma):
    if random.random() < TASA_MUTACION:
        cromosoma[random.randint(0, len(cromosoma) - 1)] = random.randint(0, 1)
    return cromosoma


def crossover(cromosoma1, cromosoma2):
    punto = random.randint(1,4)
    hijo1 = cromosoma1[:punto] + cromosoma2[punto:]
    hijo2 = cromosoma2[:punto] + cromosoma1[punto:]
    return mutacion(hijo1), mutacion(hijo2)


def reemplazo(poblacion_inicial, porcentaje_seleccion):
    padres = selection(poblacion_inicial, porcentaje_seleccion)
    numero_hijos_totales = len(poblacion_inicial) - len(padres)
    hijos = []
    contador_hijos = 0
    while contador_hijos < numero_hijos_totales:
        papa, mama = random.sample(padres, 2)
        hijo1, hijo2 = crossover(papa[0], mama[0])
        hijos.append(hijo1)
        hijos.append(hijo2)
        contador_hijos += 2
    return padres + aplicar_fitness(hijos)


def calculo_media(lista_cromosomas):
    longitud = len(lista_cromosomas)
    suma = functools.reduce(lambda i, x: i + x[1], lista_cromosomas, 0)
    return suma/longitud


def main():
    poblacion_actual = gen_population(POBLACION_TOTAL)
    poblacion_fitness = aplicar_fitness(poblacion_actual)
    print(poblacion_fitness[:10])
    for i in range(NUMERO_GENERACIONES):
        print(i)
        poblacion_fitness = reemplazo(poblacion_fitness, PORCENTAJE_SELECCION)
        print(calculo_media(poblacion_fitness))

if __name__ == "__main__":
    main()