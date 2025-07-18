import random
import timeit
import time

def subconjunto_factible_aproximacion(A, B):
    inicio = time.perf_counter()
    A_ordenado = sorted(A, reverse=True)
    
    S1 = []
    T1 = 0
    for elemento in A_ordenado:
        if T1 + elemento <= B:
            S1.append(elemento)
            T1 += elemento
    
    S2 = []
    T2 = 0
    for elemento in A_ordenado:
        if elemento <= B and elemento not in S1:
            S2 = [elemento]
            T2 = elemento
            break
    
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    print(f"Tiempo subconjunto_factible_aproximacion: {tiempo_ms} ms")
    if T1 >= T2:
        return S1
    else:
        return S2


def probar_algoritmos(A, B):
    print(f"Dataset: A={A}, B={B}")
    print("subconjunto_factible_aproximacion:", subconjunto_factible_aproximacion(A, B))
    print("-" * 40)

def main():
    with open("datasets.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            A_str, B_str = line.strip().split(";")
            A = [int(x) for x in A_str.split(",")]
            B = int(B_str)
            probar_algoritmos(A,B)

if __name__ == "__main__":
    main()