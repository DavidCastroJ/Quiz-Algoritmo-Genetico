import random
import datetime


def generar_poblacion_inicial(tamano, conjunto_genes):
    genes = []
    while(len(genes) < tamano):
        genes.extend(random.sample(conjunto_genes, min(tamano-len(genes), len(conjunto_genes))))
    return ''.join(genes)

def fitness(propuesta, resultado_objetivo):
    return sum(1 for index in range(len(resultado_objetivo)) if propuesta[index] == resultado_objetivo[index])

def mutar(padre, genes, resultado_objetivo):
    index = random.randrange(0, len(padre))
    if (resultado_objetivo[index] != padre[index]):
        padre = padre[:index] + genes[random.randrange(0, len(genes))] + padre[index+1:]
    return padre

def mostrar(propuesta, tiempo_inicio, resultado_objetivo, mostrar_anterior):
    tiempo_transcurrido = datetime.datetime.now() - tiempo_inicio
    print(f'{propuesta}, fitness: {fitness(propuesta, resultado_objetivo)}, tiempo: {str(tiempo_transcurrido)}', end='\n' if mostrar_anterior else '\r')

def run(conjunto_genes, resultado_objetivo, mostrar_anterior):
    tiempo_inicio = datetime.datetime.now()
    padre = generar_poblacion_inicial(len(resultado_objetivo), conjunto_genes)
    fitness_padre = fitness(padre, resultado_objetivo)
    numero_propuesta = 1
    while(True):
        hijo = mutar(padre, conjunto_genes, resultado_objetivo)
        fitness_hijo = fitness(hijo, resultado_objetivo)
        if (fitness_padre >= fitness_hijo):
            if(mostrar_anterior):
                print(f'propuesta #{numero_propuesta}')
            mostrar(hijo, tiempo_inicio, resultado_objetivo, mostrar_anterior)
        if (fitness_hijo >= len(padre)):
            print(''*200)
            print(f'propuesta #{numero_propuesta}')
            mostrar(hijo, tiempo_inicio, resultado_objetivo, False)
            print('')
            break
        fitness_padre = fitness_hijo
        padre = hijo
        numero_propuesta = numero_propuesta + 1

if __name__ == '__main__':
    conjunto_genes = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚüÜ"
    resultado_objetivo = "Carlos Andres Serna Lazaro"
    mostrar_anterior = False
    run(conjunto_genes, resultado_objetivo, mostrar_anterior)
