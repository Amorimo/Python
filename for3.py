num=[]
for p in range(1,6):
    v=int(input(f"Digite o {p}º número: " ))
    # Adicionar o valor de V na lista num
    num.append(v)
    for x in num:
        print(x,end="-")