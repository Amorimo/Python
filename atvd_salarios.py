
salario=float(input("Digite o salário atual do colaborador: "))

percentual=0
aumento=0

if salario<=280:
    percentual=20
    aumento=salario*percentual/100

elif salario<=700:
    percentual=15
    aumento=salario*percentual/100

elif salario<=1500:
    percentual=10
    aumento=salario*percentual/100
    
else:
    percentual=5
    aumento=salario*percentual/100


reajuste=salario +aumento

print(f"Salário antes do reajuste: R${salario}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R${aumento}")
print(f"Novo salário após o aumento: R${reajuste}")