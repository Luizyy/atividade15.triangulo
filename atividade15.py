# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

mdd1 = float(input("Digite á primeira medida:"))
mdd2 = float(input("Digite á segunda medida:"))
mdd3 = float(input("Digite á segunda medida:"))

if mdd1 < mdd2 + mdd3 and mdd2 < mdd1 + mdd3 and mdd3 < mdd1 + mdd2:
   print("É um triangulo")
else:
    print("Não é um triangulo'") 