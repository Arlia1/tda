import random
import time

def generar_set_de_datos(n, semilla=42):
    random.seed(semilla)
    ofertas = list(range(1, n + 1))
    random.shuffle(ofertas)
    return ofertas

def seleccionar_mejor_oferta(ofertas):
    n = len(ofertas)
    r = n // 2 

    mejor_observada = max(ofertas[:r])
    
    for i in range(r, n):
        if ofertas[i] > mejor_observada:
            return ofertas[i]
    
    return ofertas[-1]

def ofertas_com_semilla(n, semilla):
    ofertas = generar_set_de_datos(n, semilla)
    
    inicio = time.time()
    seleccion = seleccionar_mejor_oferta(ofertas)
    fin = time.time()
    
    tiempo = fin - inicio
    maxima = max(ofertas)
    acierto = seleccion == maxima

    print(f"Tamaño del set: {n}")
    print(f"Oferta seleccionada: {seleccion}")
    print(f"Máxima oferta: {maxima}")
    print(f"Acierto: {'Sí' if acierto else 'No'}")
    print(f"Tiempo de ejecución: {tiempo:.6f} segundos")

    return {
        "seleccion": seleccion,
        "maxima": maxima,
        "acierto": acierto,
        "tiempo": tiempo
    }

if __name__ == "__main__":
    ofertas_com_semilla(n=15, semilla=123)
