from typing import List


def media(array) -> float:
    tamanhoArr = len(array)
    somatoria = 0
    for n in array:
        somatoria += n
    return somatoria / tamanhoArr


lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 8000]

print("Media Comum: " + str(media(lista)))


def mediana(array) -> float:
    array = sorted(array)
    tamanho = len(array)
    if (tamanho % 2 == 1):
        return array[tamanho // 2]
    else:
        anterior = array[(tamanho // 2) - 1]
        posterior = array[tamanho // 2]
        return (anterior + posterior) / 2


print("Mediana truncada: " + str(mediana(lista)))


def media_trunc(array, porcentagem) -> float:
    array = sorted(array)

    #Qual é a porcentagem selecionada em relação ao array, qual a quantidade de elementos equivalente
    remocao = int(len(array) * porcentagem // 2) # Dividindo por 1 para garantir que o resultado vai ser inteiro
    return media(array[remocao, len(array)])

print("Media truncada: " + str(media_trunc(lista, 4)))

#media truncada deu errado