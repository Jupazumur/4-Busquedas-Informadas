#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
problemas.py
------------

Tarea sobre búsquedas, donde lo que es importante es crear nuevas heurísticas

"""

import busquedas
from math import log2

# ------------------------------------------------------------
#  Desarrolla el modelo del Camión mágico
# ------------------------------------------------------------

class PbCamionMagico(busquedas.ProblemaBusqueda):
    """
    ---------------------------------------------------------------------------------
     Supongamos que quiero trasladarme desde la posición discreta $1$ hasta 
     la posicion discreta $N$ en una vía recta usando un camión mágico. 
    
     Puedo trasladarme de dos maneras:
      1. A pie, desde el punto $x$ hasta el punto $x + 1$ en un tiempo de 1 minuto.
      2. Usando un camión mágico, desde el punto $x$ hasta el punto $2x$ con un tiempo 
         de 2 minutos.

     Desarrollar la clase del modelo del camión mágico
    ----------------------------------------------------------------------------------
    
    """
    def __init__(self, meta=100):
        self.meta = meta
        self.acciones_legales = ['pie', 'camion']

    def acciones(self, estado):
        x, = estado

        if 2 * x > self.meta:
            return ['pie']
        else:
            return ['pie', 'camion']

    def sucesor(self, estado, accion):
        x, = estado

        if accion == 'pie':
            costo_local = 1
            s_n = x + 1,
        if accion == 'camion':
            costo_local = 2
            s_n = x * 2,

        return s_n, costo_local

    def terminal(self, estado):
        x, = estado
        
        return True if x == self.meta else False

    @staticmethod
    def bonito(estado):
        """
        El prettyprint de un estado dado

        """
        raise NotImplementedError('Hay que hacerlo de tarea')

# ------------------------------------------------------------
#  Desarrolla una política admisible.
# ------------------------------------------------------------
def h_1_camion_magico_helper(N):
    """
    Clausura para mantener la estructura de la comparación
    """
    def h_1_camion_magico(nodo):
        """
        Mínimo de pasos

        Bajamos el costo del camión a 1. Ahora ambos cuestan lo mismo,
        entonces lo que importa son los pasos. Como la heurística
        calcula el mínimo de pasos y el costo de una acción en el real
        es mínimo 1, la heurística siempre regresará un costo (pasos) menor.

        """
        pasos = 0
        x = nodo.estado[0]
        meta = N

        while meta > x:
            if meta % 2 == 0 and meta/2 >= x:
                pasos += 1
                meta //= 2
            elif meta % 2 == 0 and meta-1 >= x:
                pasos += 1
                meta -= 1
            elif meta % 2 != 0 and meta-1 >= x:
                pasos += 1
                meta -= 1

        return pasos
    
    return h_1_camion_magico
                
# ------------------------------------------------------------
#  Desarrolla otra política admisible.
#  Analiza y di porque piensas que es (o no es) dominante una
#  respecto otra política
# ------------------------------------------------------------
def h_2_camion_magico_helper(N):
    """
    Clausura para mantener la estructura de la comparación
    """
    def h_2_camion_magico(nodo):

        """
        Pasos exactos

        Aquí se relaja aún más, ahora no solo todo cuesta uno,
        ahora podemos dar pasos exactos en camión para llegar a N.
        Multiplicamos x por 2 k veces para llegar a N.
        x * 2^k = N
        Entonces lo que nos interesa son los pasos (k),
        despejamos:
        log_2(2^k) = log_2(N / x) ---> k = log_2(N / x)
        donde k es la cantidad exacta de veces a multiplicar
        x * 2 para llegar a N

        """
        x = nodo.estado[0]

        return log2(N/x)
    
    return h_2_camion_magico

# Conclusión
# La primer heurística es dominante respecto a la segunda porque la segunda es demasiado optimista.
# La primera respeta las reglas del espacio del juego: toma en cuenta que se puede caminar e ir en
# camión. Esto hace que se aproxime más al costo real. La segunda solo toma en cuenta el camión y
# los pasos se vuelven muy pequeños debido al logaritmo. También se puede observar en los resultados,
# donde a* + h1 explora muchos menos nodos que a* + h2.

# ------------------------------------------------------------
#  Desarrolla el modelo del cubo de Rubik
# ------------------------------------------------------------

class PbCuboRubik(busquedas.ProblemaBusqueda):
    """
    La clase para el modelo de cubo de rubik, documentación, no olvides poner
    la documentación de forma clara y concisa.
    
    https://en.wikipedia.org/wiki/Rubik%27s_Cube
    
    """
    def __init__(self):
        raise NotImplementedError('Hay que hacerlo de tarea')

    def acciones(self, estado):
        raise NotImplementedError('Hay que hacerlo de tarea')

    def sucesor(self, estado, accion):
        raise NotImplementedError('Hay que hacerlo de tarea')

    def terminal(self, estado):
        raise NotImplementedError('Hay que hacerlo de tarea')

    @staticmethod
    def bonito(estado):
        """
        El prettyprint de un estado dado

        """
        raise NotImplementedError('Hay que hacerlo de tarea')

# ------------------------------------------------------------
#  Desarrolla una política admisible.
# ------------------------------------------------------------
def h_1_problema_1(nodo):
    """
    DOCUMENTA LA HEURÍSTICA QUE DESARROLLES Y DA UNA JUSTIFICACIÓN
    PLATICADA DE PORQUÉ CREES QUE LA HEURÍSTICA ES ADMISIBLE

    """
    return 0

# ------------------------------------------------------------
#  Desarrolla otra política admisible.
#  Analiza y di porque piensas que es (o no es) dominante una
#  respecto otra política
# ------------------------------------------------------------
def h_2_problema_1(nodo):
    """
    DOCUMENTA LA HEURÍSTICA DE DESARROLLES Y DA UNA JUSTIFICACIÓN
    PLATICADA DE PORQUÉ CREES QUE LA HEURÍSTICA ES ADMISIBLE

    """
    return 0

def compara_metodos(problema, pos_inicial, heuristica_1, heuristica_2):
    """
    Compara en un cuadro lo nodos expandidos y el costo de la solución
    de varios métodos de búsqueda

    @param problema: Un objeto del tipo ProblemaBusqueda
    @param pos_inicial: Una tupla con una posicion inicial
    @param heuristica_1: Una función de heurística
    @param heuristica_2: Una función de heurística

    """
    solucion1 = busquedas.busqueda_A_estrella(problema, pos_inicial, heuristica_1, )
    solucion2 = busquedas.busqueda_A_estrella(problema, pos_inicial, heuristica_2, )
    
    print('-' * 50)
    print('Método'.center(12) + 'Costo'.center(18) + 'Nodos visitados'.center(20))
    print('-' * 50 + '\n')
    print('A* con h1'.center(12) 
          + str(solucion1.costo).center(18) 
          + str(solucion1.nodos_visitados))
    print('A* con h2'.center(12) 
          + str(solucion2.costo).center(20) 
          + str(solucion2.nodos_visitados))
    print('-' * 50 + '\n')

if __name__ == "__main__":

    # Compara los métodos de búsqueda para el problema del camión mágico
    # con las heurísticas que desarrollaste
    pos_inicial = (1,)
    problema = PbCamionMagico(1000)
    compara_metodos(problema, pos_inicial, h_1_camion_magico_helper(problema.meta), h_2_camion_magico_helper(problema.meta))
    
    # Compara los métodos de búsqueda para el problema del cubo de rubik
    # con las heurísticas que desarrollaste
    #pos_inicial = XXXXXXXXXX  # <--- PONLE LA POSICIÓN INICIAL QUE QUIERAS
    #problema = PbCuboRubik( XXXXXXXXXX )  # <--- PONLE LOS PARÁMETROS QUE NECESITES
    #compara_metodos(problema, h_1_problema_1, h_2_problema_1)