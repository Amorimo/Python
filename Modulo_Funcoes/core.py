def somaLista(valores=[]):
    """
    A função somaÇista, recebe uma lista de números e faz a soma de todos os números da lista e retorna o resultado da somaLista

    Paramaters
    -----------------------
    valores: int[]
        Lista de números para a soma
    Returns
    -----------------------
        Retirba a soma de uma lista
    """
    resultado=0
    for i in valores:
        resultado+=i
    return resultado
def maiorValor(lista=[]):
    """
    A função maiorValor encontra o maior valor em uma lista numérica

    Parameters
    -----------------------
        lista:int[]
    Returns
    -----------------------
        Retorna o maior valor da lista
    """
    m=lista[0]
    for i in lista:
        if i>m:
            m=i
    return m
def inverter(palavra=""):
    # Vamos utilizar o comando len (length) para obter a quantidade da palavra
    qtd=len(palavra)
    invertdida=""
    for i in range(qtd-1,-1,-1):
        invertdida+=palavra[i]
    return invertdida
def palindromo(palavra=""):
    org=inverter(palavra).lower()
    if palavra.lower()==org:
        return "É um palindromo"
    else:
        return "Não é um palindromo"