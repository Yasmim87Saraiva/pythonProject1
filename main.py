#entrada
valor_por_hora = float(input("Qual valor vc ganha por hora? "))
Horas_trabalhadas = int(input("Quantas horas vc trabalhou nesse mês? "))
#processamento
salario = (valor_por_hora * Horas_trabalhadas)

#saida
print("Nesse mês você ira receber R${0:.2f}".format(salario))