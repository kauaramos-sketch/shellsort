def shell_sort(n):
    sort = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in sort:
        for i in range(gap, len(n)):
            temp = n[i]
            j = i
            while j >= gap and n[j - gap] > temp:
                n[j] = n[j - gap]
                j -= gap
            n[j] = temp
    return n

print("Digite os números separados por vírgula:")
entrada = input()
numeros = [int(x) for x in entrada.split(',')]
print("Números ordenados:", shell_sort(numeros))