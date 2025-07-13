import numpy as np
import matplotlib.pyplot as plt
def entrada():
    n0 = int(input("Digite n0 (Indice inicial): "))
    opcao = input("Você sabe se a série é convergente? (Digite 'a' para sim e 'b' para não): ").strip().lower() 
    if opcao == 'a':
        S = float(input("Digite a soma S: "))
        e = float(input("Digite o valor de tolerância e: "))
        Kmin = int(input(f"Digite o valor de Kmin (>= {n0}): "))
        Kmax = int(input(f"Digite o valor de Kmax (> {Kmin}, de preferência Kmax - Kmin <= 20): "))
        return n0, opcao, S, e, Kmin, Kmax 
    elif opcao == 'b':
        Kmin = int(input(f"Digite o valor de Kmin (>= {n0}): "))
        Kmax = int(input(f"Digite o valor de Kmax (> {Kmin}, de preferência Kmax - Kmin <= 20): "))
        return n0, opcao, None, None, Kmin, Kmax
    else:
        raise ValueError ("Opção inválida!")

def a(n):
    return (-1)**n / (n+1)

def calcula_serie(n0, Kmin, Kmax):
    Ks = np.arange(Kmin, Kmax+1)
    termos = np.array([a(k) for k in Ks])
    soma_parcial = np.array([sum(a(n) for n in range(n0, k+1)) for k in Ks])
    return Ks, termos, soma_parcial

def imprime_tabela(ks, valores, nome_coluna):
    print(f"\n Tabela {nome_coluna}:")
    print(f"{'K':>5} | {nome_coluna:>12}")
    print("-"*22)
    for k, v in zip(ks, valores):
        print(f"{k:5d} | {v:12.6f}")

def plota(ks, termos, soma_parcial, opcao, S=None, e=None):
    plt.figure(figsize=(8,5))
    plt.scatter(ks, termos, label='a(k)', marker='o')
    plt.scatter(ks, soma_parcial, label='S(k)', marker='s')
    if opcao == 'a':
        plt.hlines([S-e, S, S+e], ks[0], ks[-1],
                   linestyles=['--','-','--'], label='S+-e / S')
    plt.xlabel('k')
    plt.ylabel('Valores')
    plt.title('Termos e sequências e Somas parciais')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    n0, opcao, S, e, Kmin, Kmax = entrada()
    Ks, termos, soma_parcial = calcula_serie(n0, Kmin, Kmax)
    
    # (i) tabela de (k, a(k))
    imprime_tabela(Ks, termos, 'a(k)')
    
    # (ii) tabela de (k, S(k))
    imprime_tabela(Ks, soma_parcial, 'S(k)')
    
    # (iii) e (iv) gráfico
    plota(Ks, termos, soma_parcial, opcao, S, e)

if __name__ == '__main__':
    main()