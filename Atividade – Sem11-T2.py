n = 0
soma = 0
cont = 0
lista = []
try:
    while n < 999:
        x = int(input(""))
        lista.append(x)
        soma = soma + x
        n = n + 1
        if x == 0:
            lista.remove(0)
            cont = len(lista)
            media = soma / cont
            print(cont)
            print(format(media, '.2f'))
            print(min(lista))
            print(max(lista))
            break

except:
    pass
