import numpy as np
from sympy import fibonacci
import time
import sys

PHI = (1 + 5**0.5) / 2

def simular_reator_industrial():
    temp_ignicao = 150.0 
    temp_atual = 20.0
    decorrencia_acumulada = 0.0
    sucesso_longo_prazo = True

    print("\n" + "="*60)
    print(" PROJETO QUANTUM ATÔMICO: TESTE DE CARGA INDUSTRIAL ")
    print(" Escala Vyctor Brito I - Simulação de 1.000 Ciclos ")
    print("="*60 + "\n")

    for ciclo in range(1, 1001):
        # Cálculo de Fibonacci com precisão arbitrária via Sympy
        f_n = fibonacci(ciclo)
        fase_quantum = np.sin(float(f_n) / PHI)
        
        # A entropia agora cresce exponencialmente com o tempo de operação
        caos_operacional = (temp_atual / 60.0) + (ciclo / 500.0) + np.random.uniform(0.1, 1.0)
        
        # INTERVENÇÃO VYCTOR BRITO: O Escudo Quântico
        if fase_quantum < 0:
            # O tempo negativo atua como um sumidouro de entropia
            correcao = abs(fase_quantum) * 15.0
            decorrencia_acumulada -= correcao
            status = "[ESCUDO]"
        else:
            decorrencia_acumulada += caos_operacional
            status = "[FLUXO ]"

        decorrencia_acumulada = max(0, decorrencia_acumulada)
        estabilidade = max(0, 100.0 - decorrencia_acumulada)
        
        # Mantém a temperatura no ápice após a ignição
        if temp_atual < temp_ignicao:
            temp_atual += (2.0 - (decorrencia_acumulada / 70.0))
        else:
            temp_atual = temp_ignicao + np.sin(ciclo) # Oscilação térmica controlada

        # Monitoramento a cada 10 ciclos para evitar lentidão no Termux
        if ciclo % 10 == 0 or estabilidade < 20:
            sys.stdout.write(f"\rCiclo {ciclo:04d} | Temp: {temp_atual:6.2f}MK | Estabilidade: {estabilidade:5.2f}% | {status}")
            sys.stdout.flush()
            time.sleep(0.02)

        if estabilidade <= 0:
            print(f"\n\n[COLAPSO TÉRMICO] Falha estrutural no ciclo {ciclo}.")
            sucesso_longo_prazo = False
            break

    if sucesso_longo_prazo:
        print(f"\n\n[OPERAÇÃO COMERCIAL VALIDADA]")
        print(f"O reator operou por 1.000 ciclos sob a Escala Vyctor Brito I.")
        print(f"Estabilidade Final: {estabilidade:.2f}%")

simular_reator_industrial()
