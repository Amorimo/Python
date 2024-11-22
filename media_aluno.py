media=float(input("Digite a média do aluno: "))
if media >=6:
    print(f"Aluno com média {media} está Aprovado")
elif media <=4:
    print(f"Aluno com média {media} está Reprovado")
else:
    print(f"Aluno com média {media} está em Recuperação")